from aws_learn.sqs.sqs import send, receive
from typing import Union, Literal

import argparse


UsageType = Union[Literal["send"], Literal["receive"]]


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, choices=["send", "receive"], required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    if args.type == "send":
        send()
    elif args.type == "receive":
        receive()
    else:
        raise Exception("bad arg")
