# Kafka + FastAPI High-Throughput Ingestion System

This project demonstrates a scalable event ingestion pipeline using **FastAPI**, **Apache Kafka**, **Zookeeper**, and **Docker**. It simulates high-throughput API traffic and processes events asynchronously using Kafka.

---

## 🧩 Architecture Overview

[FastAPI Producer] --> [Kafka Topic: events] --> [Kafka Consumer] --> [Logging / Processing]
^
[Zookeeper + Kafka (Docker)]


---

## 📦 Project Structure

kafka-api-ingestion/
│
├── app/
│ ├── main.py # FastAPI server with /register_event and /get_status
│
├── consumer/
│ ├── consumer.py # Kafka consumer that logs incoming events
│ └── consumer.log # Output log of processed events
│
├── simulate/
│ ├── simulate_traffic.py # Script to simulate 10,000 event POSTs
│
├── docker-compose.yml # Sets up Kafka + Zookeeper
├── README.md # This file
└── summary.md # Project summary


---

## 🚀 How to Run

### 1️⃣ Start Kafka and Zookeeper
```bash
docker-compose up -d

2️⃣ Start FastAPI Server

cd app
uvicorn main:app --reload

3️⃣ Start Kafka Consumer

cd consumer
python consumer.py


4️⃣ Simulate Traffic


cd simulate
python simulate_traffic.py

🔁 API Endpoints
POST /register_event
Accepts a JSON event and pushes it to Kafka.

{
  "event_id": "abc123",
  "event_type": "click",
  "payload": {
    "user_id": "user_1",
    "action": "open_app"
  }
}

GET /get_status
Health check endpoint:

{"status": "API is running"}


📈 What It Demonstrates
Handling high-throughput requests (10,000+)

Asynchronous event-driven architecture

Kafka integration with FastAPI

Logging processed events

Dockerized microservices setup

🛠 Requirements
Python 3.8+

Docker & Docker Compose

kafka-python, fastapi, uvicorn, requests

🧠 Learning Goals
Scalable API ingestion via Kafka

Decoupling producers and consumers

Real-world traffic simulation

Logging and observability practices