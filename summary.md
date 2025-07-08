#  Project Summary: Kafka-Based API Ingestion with FastAPI

##  Objective

This project demonstrates how to build a scalable, event-driven system using **FastAPI**, **Kafka**, and **Zookeeper**. The goal is to simulate high-throughput traffic (10,000 requests) and process events asynchronously using Kafka consumer workers.

---

##  Tech Stack

- **FastAPI**: Handles incoming HTTP POST requests (event ingestion).
- **Apache Kafka**: Asynchronous message queue for decoupling producer/consumer.
- **Zookeeper**: Manages Kafka coordination and broker metadata.
- **Docker Compose**: Launches Kafka + Zookeeper containers.
- **Kafka-Python**: Produces and consumes events in Python.
- **Uvicorn**: ASGI server to run FastAPI.
- **Requests**: Used for traffic simulation.

---

##  Data Flow

1. `simulate_traffic.py` sends 10,000 POST requests to FastAPI (`/register_event`).
2. FastAPI validates and sends each request to a Kafka topic named `events`.
3. Kafka stores the messages and manages offset tracking.
4. A Kafka consumer (`consumer.py`) subscribes to the `events` topic.
5. Each message is read from Kafka and logged to `consumer.log`.

---

##  Use Case Demonstration

 Handles thousands of API requests efficiently  
 Demonstrates event decoupling using Kafka  
 Real-time log generation for each processed event  
 Works as a blueprint for IoT data pipelines, logs, telemetry, etc.

---

##  Features Simulated

- High-volume traffic generation (10,000 events)
- Message validation and queuing
- Asynchronous decoupling of ingest and processing
- Real-time logging for observability

---

##  Folder Overview

| Path                     | Description                            |
|--------------------------|----------------------------------------|
| `app/main.py`            | FastAPI producer app                   |
| `consumer/consumer.py`   | Kafka consumer with message logging    |
| `consumer/consumer.log`  | Output logs of consumed messages       |
| `simulate/simulate_traffic.py` | Traffic simulator (10,000 requests) |
| `docker-compose.yml`     | Kafka and Zookeeper container setup    |

---

##  Outcome

- Kafka successfully buffers traffic from FastAPI.
- Consumer logs show correct message processing.
- FastAPI endpoint resilient to heavy concurrent requests.
- Demonstrates the architecture of scalable ingestion systems.

---

##  Next Steps

- Integrate message persistence (e.g., MongoDB/PostgreSQL).
- Add retry logic in case of Kafka downtime.
- Add metrics/logging using Prometheus + Grafana.
- Extend simulation with realistic, randomized event data.
