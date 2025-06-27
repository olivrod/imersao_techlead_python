import boto3
import sys
import csv
import tempfile
import io

#python3 processa_boletos.py 42sp-matherib-boletos boletos_0000.csv
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

def main()->None:
    if len(sys.argv) > 2:
        bucket = sys.argv[1]
        key = sys.argv[2]
        print(f'Processando {bucket} {key}')
        
        with tempfile.NamedTemporaryFile('w+b') as csvfile:
            s3 = boto3.client('s3')
            s3.download_fileobj(bucket, key, csvfile)
            csvfile.seek(0)
            csv_reader = csv.DictReader(io.TextIOWrapper(csvfile, encoding='utf-8'))
            
            load(csv_reader)
    

if __name__ == "__main__":
    main()