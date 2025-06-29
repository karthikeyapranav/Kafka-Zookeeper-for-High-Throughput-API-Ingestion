from fastapi import FastAPI
from pydantic import BaseModel
from kafka import KafkaProducer
import json
import os

KAFKA_TOPIC = "events"
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

app = FastAPI()

# Define expected structure
class RegisterEvent(BaseModel):
    event_id: str
    event_type: str
    payload: dict

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.post("/register_event")
def register_event(event: RegisterEvent):
    producer.send(KAFKA_TOPIC, value=event.dict())
    return {"status": "Event published"}

@app.get("/get_status")
def get_status():
    return {"status": "API is running"}
