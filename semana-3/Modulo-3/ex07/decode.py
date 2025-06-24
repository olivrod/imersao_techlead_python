import base64
import boto3
import uuid

def decode_image(base64_str: str) -> bytes:
    """
    Decode a base64 encoded image string into bytes.
    """
    return base64.b64decode(base64_str)

def decode_and_upload(base64_str, bucket_name):
    base64_str = base64_str.replace('data:image/jpeg;base64,', '')
    image_bytes = decode_image(base64_str)
    if not image_bytes:
        raise ValueError("No image data found in the provided string.")
    image_file_name_jpg = f"{uuid.uuid4()}.jpg"
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket_name, Key=image_file_name_jpg, Body=image_bytes, ContentType="image/jpeg")
    return image_file_name_jpg

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("Uso: python3 decode.py <bucket_name> <base64_image_txt_path>")
#         sys.exit(1)

#     bucket_name = sys.argv[1]
#     txtfilepath = sys.argv[2]

#     if not txtfilepath.endswith(".txt"):
#         print("Please provide a .txt file containing the base64 encoded image.")
#         sys.exit(1)

#     with open(txtfilepath, "r") as f:
#         base64_str = f.read()
#         image_file_name_jpg = decode_and_upload(base64_str, bucket_name)
#         print(f"'{image_file_name_jpg}' saved on bucket '{bucket_name}'!")