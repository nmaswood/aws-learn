from aws_learn.chalice import app
from aws_learn.kafka import produce, consume


def hello_world():
    return {"hello": "world"}
