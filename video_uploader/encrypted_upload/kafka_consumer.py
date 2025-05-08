# kafka_consumer.py

from kafka import KafkaConsumer
import json
from django.conf import settings

def start_kafka_consumer():
    consumer = KafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='video-consumers',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    print("Kafka consumer started. Waiting for messages...")

    for message in consumer:
        data = message.value
        print(f"Received video upload message: {data}")
        # Add further processing logic here (e.g., start transcoding, notify frontend, etc.)
