import os

from chalice import Chalice
import aws_learn as A

app = Chalice(app_name="39 Queue")


@app.route("/ping")
def index():
    return "pong"


QUEUE_NAME = os.environ["SQS_QUEUE_NAME"]


@app.on_sqs_message(queue=QUEUE_NAME)
def handler(event):
    for record in event:
        print(record

