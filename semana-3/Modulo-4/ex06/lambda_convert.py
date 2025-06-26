import boto3
from PIL import Image
import io

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Extrai informações do evento
    record = event['Records'][0]
    src_bucket = record['s3']['bucket']['name']
    src_key = record['s3']['object']['key']
    dst_bucket = src_bucket + "-converted"
    dst_key = src_key

    # Baixa a imagem original do bucket de origem
    response = s3.get_object(Bucket=src_bucket, Key=src_key)
    image_content = response['Body'].read()

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

    # Salva a imagem processada no bucket de destino
    s3.put_object(Bucket=dst_bucket, Key=dst_key, Body=buffer, ContentType="image/jpeg")

    return {"statusCode": 200, "body": f"Converted {src_key} and saved to {dst_bucket}/{dst_key}"}