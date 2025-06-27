aws lambda delete-function --function-name processa_boletos_lambda 

mkdir package
# docker run --rm -v "$PWD":/var/task \
#     --entrypoint /bin/sh \
#     public.ecr.aws/lambda/python:3.13 \
#    -c "pip install pillow -t package/"
cp ../ex04/processa_boletos_lambda.py package/
(cd package && zip -r ../package.zip .)

aws lambda create-function \
    --function-name processa_boletos_lambda \
    --handler processa_boletos_lambda.lambda_handler \
    --zip-file fileb://package.zip \
    --runtime python3.13 \
    --role arn:aws:iam::000000000000:role/lambda-role \
    --timeout 900 \
    --no-cli-pager

rm package.zip
rm -rf package

aws lambda add-permission \
    --function-name processa_boletos_lambda \
    --action lambda:InvokeFunction \
    --statement-id sqs \
    --principal sqs.amazonaws.com 

aws lambda create-event-source-mapping \
    --function-name processa_boletos_lambda \
    --event-source-arn arn:aws:sqs:us-east-1:000000000000:42sp-MATHERIB-queue

#python3 upload_boletos.py ../remessas/boletos_0003.csv 
#aws dynamodb scan --table-name Boletos