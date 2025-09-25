from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'location-events',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='connection-service',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def consume_location_events():
    for message in consumer:
        location_data = message.value
        print("New location event is received as: ", location_data)
        
