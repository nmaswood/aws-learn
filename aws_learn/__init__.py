from kafka import KafkaConsumer, KafkaProducer

BOOTSTRAP = ['192.168.64.2:32554']

consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_servers=BOOTSTRAP)

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP)




future = producer.send('nasr', b'raw_bytes')

record_metadata = future.get(timeout=5)

