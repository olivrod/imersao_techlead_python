import sys
import boto3

def receive_message(queue_url):
    """
    Read the message from a given SQS queue every 10 seconds and remove it from the queue.

    :param queue_url: The URL of the SQS queue.
    :return: The received message or None if no messages are available.
    """
    
    print("Aguardando mensagens...")

    # Create an SQS client
    sqs = boto3.client('sqs')

    # Receive a message from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        WaitTimeSeconds=10,  # Long polling for 10 seconds
        MaxNumberOfMessages=10,  # Receive only one message at a time
    )

    messages = response.get('Messages', [])
    
    if not messages:
        return None

    for message in messages:
        print(f"Mensagem recebida: {{'message': '{message.get('Body')}'}}")
        # Delete the message from the queue after processing
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

    return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python receive_message.py <queue_url>")
        sys.exit(1)

    queue_url = sys.argv[1]

    while True:      
        receive_message(queue_url)

# dev: python3 receive_message.py 'http://localhost:4566/000000000000/42sp-admitsun-queue.fifo'
# prod: python3 receive_message.py 'https://sqs.us-east-1.amazonaws.com/533252222381/42sp-admitsun-queue.fifo'
