from aws_learn.kafka.kafka import produce, consume
from typing import Union, Literal

import argparse


UsageType = Union[Literal["producer"], Literal["consumer"]]


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type", type=str, choices=["consumer", "producer"], required=True
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    if args.type == "consumer":
        consume()
    elif args.type == "producer":
        produce()
    else:
        raise Exception("bad arg")
