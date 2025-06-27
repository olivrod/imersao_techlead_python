import boto3 
import sys
import os
#aws s3api list-objects --bucket '42sp-matherib-boletos' --no-cli-pager
#python3 upload_boletos.py ../remessas/boletos_0000.csv 
def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        bucket = "42sp-matherib-boletos"

        with open(path, 'rb') as file:
            s3 = boto3.client('s3')
            key = os.path.basename(path)

            s3.put_object(Body=file,
                        Bucket=bucket,
                        Key=key)
            
            print(f'Upload realizado com sucesso: {key}')


if __name__ == "__main__":
    main()