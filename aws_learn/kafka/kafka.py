import json

from confluent_kafka import Producer, Consumer

from aws_learn.kafka.Constants import DEFAULT_TOPIC, CONFIG


def consume():
    c = Consumer({**CONFIG, **{"group.id": "consumer-1"}})

    c.subscribe([DEFAULT_TOPIC])

    total_count = 0
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                print("Message was none")
                continue
            elif msg.error():
                print("error: {}".format(msg.error()))
            else:
                # Check for Kafka message
                record_key = msg.key()
                record_value = msg.value()
                data = json.loads(record_value)
                count = data["count"]
                total_count += count
                print(
                    "Consumed record with key {} and value {}, \
                      and updated total count to {}".format(
                        record_key, record_value, total_count
                    )
                )
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        c.close()

    print("Let's start consuming")


def produce():
    p = Producer(CONFIG)

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
            print(
                "Produced record to topic {} partition [{}] @ offset {}".format(
                    msg.topic(), msg.partition(), msg.offset()
                )
            )

    for n in range(10):
        record_key = "alice"
        record_value = json.dumps({"count": n})
        print("Producing record: {}\t{}".format(record_key, record_value))
        p.produce(DEFAULT_TOPIC, key=record_key, value=record_value, on_delivery=acked)

        p.poll(0)

    p.flush()

    print(
        "{} messages were produced to topic {}!".format(
            delivered_records[0], DEFAULT_TOPIC
        )
    )
