def lambda_handler(event, context):
    events = {
        'message': 'Hello from Lambda!',
        'statusCode': 200
    }
    
    return events

# aws lambda delete-function --function-name first_lambda --endpoint-url http://localhost:4566