import boto3
import sys

def send_message(queue_url, message_body):
    """
    Sends a message to the specified SQS queue.

    :param queue_url: The URL of the SQS queue.
    :param message_body: The body of the message to send.
    """
    # Create an SQS client
    sqs = boto3.client('sqs')

    # Send the message
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body,
        MessageGroupId='default-group'  # Obrigatório para filas FIFO
    )

    return response

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python send_message.py <queue_url> <message_body>")
        sys.exit(1)

    queue_url = sys.argv[1]
    message_body = sys.argv[2]

    response = send_message(queue_url, message_body)

# source ../dev.env
# python3 send_message.py http://localhost:4566/000000000000/42sp-$(whoami)-queue.fifo "Foo1"
# python3 send_message.py http://localhost:4566/000000000000/42sp-$(whoami)-queue.fifo "Foo2"
# python3 send_message.py http://localhost:4566/000000000000/42sp-$(whoami)-queue.fifo "Foo3"
# source ../prod.env
# python3 send_message.py https://sqs.us-east-1.amazonaws.com/533252222381/42sp-admitsun-queue.fifo "Foo1"
# python3 send_message.py https://sqs.us-east-1.amazonaws.com/533252222381/42sp-admitsun-queue.fifo "Foo2"
# python3 send_message.py https://sqs.us-east-1.amazonaws.com/533252222381/42sp-admitsun-queue.fifo "Foo3"