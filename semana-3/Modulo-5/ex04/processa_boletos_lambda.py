
import json
from typing import Any, Dict
import tempfile
import boto3
import csv
import io
#import traceback
#import sys

def load(csv_reader, tablename='Boletos'):
    inseridos, atualizados, ignorados = 0, 0, 0
        
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tablename)

    carregando = {}
    for row in csv_reader:
        if row['id'] in carregando:
            ignorados+=1
            continue
        elif retrieve(row['id']) is not None:
            atualizados+=1
        else:
            inseridos+=1
        carregando[row['id']] = row
        table.put_item(Item = row)
    
    print(f'Inseridos: {inseridos}\nAtualizados: {atualizados}\nIgnorados: {ignorados}')

def retrieve(id, tablename="Boletos"):
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(tablename)
    response = table.get_item(
        Key = {'id': id},
        TableName = tablename
    )

    if 'Item' in response:
        return response['Item']
    else:
        return None

def lambda_handler(event: Dict[str, Any], context: Any) -> None:
    try:
        sqs = boto3.client('sqs')
        for record in event['Records']:
            s3_records = json.loads(record['body'])

            for s3_record in s3_records['Records']:
                bucket = s3_record['s3']['bucket']['name']
                key = s3_record['s3']['object']['key']
                
                print(f'Processando {bucket} {key}')

                with tempfile.NamedTemporaryFile('w+b') as csvfile:
                    s3 = boto3.client('s3')
                    s3.download_fileobj(bucket, key, csvfile)
                    csvfile.seek(0)
                    csv_reader = csv.DictReader(io.TextIOWrapper(csvfile, encoding='utf-8'))
                    
                    load(csv_reader)
            url_fila = sqs.get_queue_url(QueueName=record['eventSourceARN'].split(':')[-1])['QueueUrl']
            sqs.delete_message(
                        QueueUrl=url_fila,
                        ReceiptHandle=record['receiptHandle']
                    )
    except Exception:
        pass
        #exc_type, exc_value, exc_traceback = sys.exc_info()
        #traceback.print_exception(exc_type, exc_value, exc_traceback)

#python3
#import json
#from processa_boletos_lambda import lambda_handler
#with open('sample_event.json', 'r') as f:
#  event = json.load(f)
#lambda_handler(event, None)