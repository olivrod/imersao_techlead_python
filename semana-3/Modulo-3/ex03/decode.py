import base64
import sys
import boto3
import os

def decode_image(base64_str: str) -> bytes:
    """
    Decode a base64 encoded image string into bytes.
    """
    return base64.b64decode(base64_str)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 decode.py <bucket_name> <base64_image_txt_path>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    txtfilepath = sys.argv[2]

    if not txtfilepath.endswith(".txt"):
        print("Please provide a .txt file containing the base64 encoded image.")
        sys.exit(1)

    with open(txtfilepath, "r") as f:
        base64_str = f.read()
        base64_str = base64_str.replace('data:image/jpeg;base64,', '')
        image_bytes = decode_image(base64_str)
        image_file_name_jpg = os.path.basename(txtfilepath).replace(".txt", ".jpg")

    if not image_bytes:
        print("No image data found in the provided file.")
        sys.exit(1)

    # Conectando ao S3 (usando Localstack se necessário)
    s3 = boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",  # Remova esta linha para AWS real
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1"
    )

    # Fazendo upload da imagem para o bucket
    s3.put_object(Bucket=bucket_name, Key=image_file_name_jpg, Body=image_bytes, ContentType="image/jpeg")
    print(f"'{image_file_name_jpg}' saved on bucket '{bucket_name}'!")
    
    
# ?> python3 decode.py "42sp-rde-oliv-bucket" "sample_images/image1.txt"
# 'image1.jpg' saved on bucket '42sp-rde-oliv-bucket'!