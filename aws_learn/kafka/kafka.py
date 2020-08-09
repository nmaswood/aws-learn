import os
from typing import Union, Literal
import json
import argparse

from confluent_kafka import Producer, Consumer



UsageType = Union[Literal['producer'], Literal['consumer']]

topic = 'nasr-test-topic'
KAFKA_KEY = os.environ['KAFKA_KEY']
KAFKA_SECRET = os.environ['KAFKA_SECRET']
KAFKA_BOOTSTRAP= os.environ['KAFKA_BOOTSTRAP']


def consume():
    c = Consumer({
        'bootstrap.servers': KAFKA_BOOTSTRAP,
        'sasl.username': KAFKA_KEY,
        'sasl.password': KAFKA_SECRET,
        'sasl.mechanism': 'PLAIN',
        'security.protocol': 'SASL_SSL',
        'group.id': 'consumer-1',
    })

    c.subscribe([topic])

    total_count = 0
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                print("Message was none")
                continue
            elif msg.error():
                print('error: {}'.format(msg.error()))
            else:
                # Check for Kafka message
                record_key = msg.key()
                record_value = msg.value()
                data = json.loads(record_value)
                count = data['count']
                total_count += count
                print("Consumed record with key {} and value {}, \
                      and updated total count to {}"
                      .format(record_key, record_value, total_count))
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        c.close()

    print ("Let's start consuming")

def produce():
    p = Producer({
        'bootstrap.servers': KAFKA_BOOTSTRAP,
        'sasl.username': KAFKA_KEY,
        'sasl.password': KAFKA_SECRET,
        'sasl.mechanism': 'PLAIN',
        'security.protocol': 'SASL_SSL',
    })

    delivered_records = [0]

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records[0] += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))

    for n in range(10):
        record_key = "alice"
        record_value = json.dumps({'count': n})
        print("Producing record: {}\t{}".format(record_key, record_value))
        p.produce(topic, key=record_key, value=record_value, on_delivery=acked)
        # p.poll() serves delivery reports (on_delivery)
        # from previous produce() calls.
        p.poll(0)

    p.flush()

    print("{} messages were produced to topic {}!".format(delivered_records[0], topic))

    print ("Let's start producing")


def parse_args():
    parser = argparse.ArgumentParser(
        description='Get n most common from a list of values')
    parser.add_argument('--type', type=str, choices=['consumer', 'producer'], required=True)

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()
    if args.type == 'consumer':
        consume()
    elif args.type == 'producer':
        produce()
    else:
        raise Exception("bad arg")


