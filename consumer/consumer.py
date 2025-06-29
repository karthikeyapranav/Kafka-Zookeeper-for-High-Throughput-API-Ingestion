from kafka import KafkaConsumer
import json
import time
import logging
import os

KAFKA_TOPIC = "events"
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Setup logging
logging.basicConfig(
    filename="../logs/consumer.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def process_message(msg):
    # Simulate error randomly
    if msg.get("fail") == True:
        raise Exception("Simulated processing error")
    logging.info(f"Processed message: {msg}")

def run():
    for message in consumer:
        data = message.value
        retries = 3
        while retries > 0:
            try:
                process_message(data)
                break
            except Exception as e:
                retries -= 1
                logging.error(f"Error: {e}, Retries left: {retries}")
                time.sleep(1)

if __name__ == "__main__":
    run()
