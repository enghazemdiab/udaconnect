from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_location_event(location_data):
    producer.send('location-events', value=location_data)
    producer.flush()
