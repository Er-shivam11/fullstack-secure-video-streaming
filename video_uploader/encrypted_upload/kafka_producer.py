# kafka_producer.py
from kafka import KafkaProducer
import json
from django.conf import settings

_producer = None

def get_kafka_producer():
    global _producer
    if _producer is None:
        _producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    return _producer

def send_video_upload_message(video_id, filename, title):
    try:
        message = {
            "video_id": video_id,
            "filename": filename,
            "title": title
        }
        producer = get_kafka_producer()
        producer.send(settings.KAFKA_TOPIC, value=message)
        producer.flush()
    except Exception as e:
        print(f"Kafka error: {e}")

