import logging
import boto3
from PIL import Image
import io

# Configura o logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Extrai informações do evento
    record = event['Records'][0]
    src_bucket = record['s3']['bucket']['name']
    src_key = record['s3']['object']['key']
    logger.info(f"Received event: {event}")
    logger.info(f"record: {record}")
    logger.info(f"Source bucket: {src_bucket}")
    logger.info(f"Processing file: {src_key}")
    dst_bucket = "42sp-rde-oliv-bucket-converted"
    dst_key = src_key

    try:
        # Verifica se o arquivo de origem existe
        s3.head_object(Bucket=src_bucket, Key=src_key)
    except s3.exceptions.ClientError as e:
        logger.error(f"Source file {src_key} does not exist in bucket {src_bucket}: {e}")
        return {"statusCode": 404, "body": f"Source file not found: {e}"}
    
    # Baixa a imagem original do bucket de origem
    response = s3.get_object(Bucket=src_bucket, Key=src_key)
    image_content = response['Body'].read()

    logger.info(f"Image {src_key} downloaded successfully from {src_bucket}.")

    try:
        # Processa a imagem
        with Image.open(io.BytesIO(image_content)) as img:
            # Redimensiona se necessário (exemplo: largura máxima 800px)
            max_width = 800
            if img.width > max_width:
                ratio = max_width / float(img.width)
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height))
            # Converte para tons de cinza
            img = img.convert('L')
            # Salva em buffer
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG")
            buffer.seek(0)
            logger.info("Image processed successfully.")
    except Exception as e:
        logger.error(f"Error processing image {src_key}: {e}")
        return {"statusCode": 500, "body": f"Error processing image: {e}"}

    try:
        # Verifica se o arquivo já existe no bucket de destino
        s3.head_object(Bucket=dst_bucket, Key=dst_key)
        logger.info(f"File {dst_key} already exists in {dst_bucket}. Overwriting.")
    except s3.exceptions.ClientError:
        logger.info(f"File {dst_key} does not exist in {dst_bucket}. Proceeding to save.")

    try:    
        # Salva a imagem processada no bucket de destino
        s3.put_object(Bucket=dst_bucket, Key=dst_key, Body=buffer, ContentType="image/jpeg")
        logger.info(f"Image {dst_key} saved to {dst_bucket}.")
    except Exception as e:
        logger.error(f"Error saving image {dst_key} to {dst_bucket}: {e}")
        return {"statusCode": 500, "body": f"Error saving image: {e}"}

    return {"statusCode": 200, "body": f"Converted {src_key} and saved to {dst_bucket}/{dst_key}"}