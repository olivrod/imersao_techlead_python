import sys
import boto3

if len(sys.argv) != 3:
    print("Uso: python3 presign.py <bucket_name> <object_key>")
    sys.exit(1)

bucket_name = sys.argv[1]
object_key = sys.argv[2]

s3 = boto3.client("s3")

# Gera a URL pré-assinada com validade de 10 minutos (600 segundos)
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=600 # 10 minutos
)

print(f"URL pré-assinada: {url}")
print("Use esta URL para acessar o objeto no S3.")
print("A URL é válida por 10 minutos.")
print("Após esse período, você precisará gerar uma nova URL.")
print("Certifique-se de que o bucket e o objeto existem e que você tem permissão para acessá-los.")
print("Se você encontrar problemas, verifique suas credenciais AWS e as permissões do bucket.")
print("Para mais informações, consulte a documentação do boto3.")

# 00366c82-5173-498d-92cd-e20faf8a90ac.jpg
# ?> python3 presign.py 42sp-rde-oliv-bucket 00366c82-5173-498d-92cd-e20faf8a90ac.jpg
# https://42sp-SEU_LOGIN-bucket.s3.amazonaws.com/882320-2939223-82823.jpg?X-Amz-Algorithm=