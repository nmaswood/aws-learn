DEFAULT_TOPIC = "nasr-test-topic"
KAFKA_KEY = os.environ["KAFKA_KEY"]
KAFKA_SECRET = os.environ["KAFKA_SECRET"]
KAFKA_BOOTSTRAP = os.environ["KAFKA_BOOTSTRAP"]

CONFIG = {
    "bootstrap.servers": KAFKA_BOOTSTRAP,
    "sasl.username": KAFKA_KEY,
    "sasl.password": KAFKA_SECRET,
    "sasl.mechanism": "PLAIN",
    "security.protocol": "SASL_SSL",
}
