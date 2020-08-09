from time import sleep

import boto3


from aws_learn.sqs.Constants import SQS_QUEUE_URL, DEFAULT_AWS_REGION


sqs = boto3.client("sqs", region_name=DEFAULT_AWS_REGION)

MESSAGE_GROUP_ID = "nasr-test"


def receive():
    print("Helo world")
    while True:
        response = sqs.receive_message(
            QueueUrl=SQS_QUEUE_URL,
            AttributeNames=["SentTimestamp"],
            MaxNumberOfMessages=1,
            MessageAttributeNames=["All"],
            VisibilityTimeout=60,
            WaitTimeSeconds=20,
        )
        if "Messages" in response:
            message = response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            sqs.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt_handle)
            print(message)
        else:
            print("no Message")
            print(response)
        sleep(10)


def send():
    for i in range(100):
        response = sqs.send_message(
            MessageGroupId=MESSAGE_GROUP_ID,
            MessageDeduplicationId=str(i),
            QueueUrl=SQS_QUEUE_URL,
            MessageAttributes={
                "Title": {"DataType": "String", "StringValue": "The Whistler"},
                "Author": {"DataType": "String", "StringValue": "John Grisham"},
                "WeeksOn": {"DataType": "Number", "StringValue": "6"},
            },
            MessageBody=(
                f"{i}-Information about current NY Times fiction bestseller for "
                "week of 12/11/2016."
            ),
        )

        print(response["MessageId"])
        sleep(15)

