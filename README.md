#  Kafka + FastAPI High-Throughput Event Ingestion System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![FastAPI Version](https://img.shields.io/badge/FastAPI-0.111.0%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-2.x%2B-blueviolet.svg)](https://kafka.apache.org/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-Up-blue.svg)](https://docs.docker.com/compose/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This project showcases a robust and scalable **event ingestion pipeline** designed for high-throughput data streams. It leverages the power of **FastAPI** for efficient API request handling, **Apache Kafka** for asynchronous event processing and decoupling, and **Docker** for simplified deployment and environment consistency.

It's a practical demonstration of how to build a system that can gracefully handle a large volume of incoming data, process it reliably, and maintain responsiveness, making it ideal for analytics, logging, or real-time data processing applications.

---

##  Architecture Overview

The system is designed with a clear separation of concerns, enabling scalability and resilience:

+-------------------+      +-----------------+      +-----------------+
| FastAPI Producer  |----->| Kafka Topic:    |----->| Kafka Consumer  |
| (HTTP/REST API)   |      |   'events'      |      | (Background Job)|
+-------------------+      +-----------------+      +-----------------+
▲                            ▲
|                            |
|      +---------------------+
|      | Zookeeper + Kafka   |
|      | (Dockerized Cluster)|
|      +---------------------+
|
+-----------------------------> Logs / Further Processing


1.  **FastAPI Producer (`app/main.py`):** Acts as the ingestion endpoint. It receives incoming events via HTTP POST requests and immediately publishes them to a Kafka topic. This allows the API to respond quickly without waiting for the actual event processing to complete, handling high concurrency.
2.  **Apache Kafka + Zookeeper (Docker):** Forms the backbone of the event bus. Kafka acts as a distributed streaming platform, capable of handling vast amounts of data. Zookeeper manages Kafka brokers. Events are reliably stored in the `events` topic.
3.  **Kafka Consumer (`consumer/consumer.py`):** Runs as a separate process, continuously listening for new messages on the `events` Kafka topic. When an event is consumed, it simulates processing by logging the event details, demonstrating how decoupled background tasks would handle the data.

This asynchronous architecture ensures that the API remains highly responsive, even under immense load, as the heavy lifting of event processing is offloaded to the Kafka consumer.

---

##  Project Structure

kafka-api-ingestion/
├── app/                        # FastAPI application (Producer)
│   ├── main.py                 # Core FastAPI server with API endpoints
│   └── requirements.txt        # Python dependencies for the FastAPI app
│
├── consumer/                   # Kafka Consumer application
│   ├── consumer.py             # Script to consume and process events from Kafka
│   ├── consumer.log            # Log file where processed events are written
│   └── requirements.txt        # Python dependencies for the consumer
│
├── simulate/                   # Traffic simulation tools
│   ├── simulate_traffic.py     # Script to generate and send high-volume POST requests
│   └── requirements.txt        # Python dependencies for the simulator
│
├── docker-compose.yml          # Docker Compose configuration for Kafka and Zookeeper
├── README.md                   # This detailed project guide (you are here!)
└── summary.md                  # A brief, high-level project summary

---

##  How to Run the System

Follow these steps to set up and run the entire high-throughput ingestion pipeline on your local machine.

### Prerequisites

Before you start, ensure you have the following installed:

* **Python 3.8+**: Essential for running the FastAPI application and Kafka consumer.
* **Docker & Docker Compose**: Necessary to easily spin up and manage Kafka and Zookeeper containers.

### Step-by-Step Execution

1.  **Start Kafka and Zookeeper Services:**
    First, bring up the Kafka and Zookeeper containers. These form the core message bus.
    Navigate to the root directory of the project (`kafka-api-ingestion/`) and run:
    ```bash
    docker-compose up -d
    ```
    * `docker-compose up -d` runs the services in detached mode (in the background).
    * Wait a few moments for Zookeeper and Kafka to fully initialize.

2.  **Install Python Dependencies:**
    Each component has its own `requirements.txt`. It's best practice to install them within a virtual environment for each respective folder.

    * **For FastAPI App:**
        ```bash
        cd app
        pip install -r requirements.txt
        cd .. # Go back to the root directory
        ```
    * **For Kafka Consumer:**
        ```bash
        cd consumer
        pip install -r requirements.txt
        cd .. # Go back to the root directory
        ```
    * **For Traffic Simulator:**
        ```bash
        cd simulate
        pip install -r requirements.txt
        cd .. # Go back to the root directory
        ```

3.  **Start the FastAPI Server (Producer):**
    This will launch your API endpoint, ready to receive events.
    ```bash
    cd app
    uvicorn main:app --reload
    ```
    * `uvicorn main:app` tells Uvicorn to run the `app` instance from `main.py`.
    * `--reload` enables auto-reloading on code changes (useful for development).
    * You should see output indicating the server is running, typically on `http://127.0.0.1:8000`.

4.  **Start the Kafka Consumer:**
    In a **new terminal window** (keep the FastAPI server running in the first one), navigate to the `consumer` directory and start the Kafka consumer.
    ```bash
    cd consumer
    python consumer.py
    ```
    * The consumer will start listening for messages. You'll see output confirming it's connected to Kafka.
    * Processed events will be logged to `consumer/consumer.log`. You can `tail -f consumer.log` in another terminal to watch events being processed in real-time.

5.  **Simulate High-Throughput Traffic:**
    In yet another **new terminal window**, navigate to the `simulate` directory and run the traffic simulation script.
    ```bash
    cd simulate
    python simulate_traffic.py
    ```
    * This script will send **10,000 POST requests** to your FastAPI endpoint, demonstrating the system's ability to handle high load.
    * You'll see output indicating the number of requests sent and the total time taken.

### Verification

* Observe the `consumer.log` file (e.g., using `tail -f consumer/consumer.log`) to see the events being processed by the consumer.
* Check the FastAPI server's terminal for any errors, though it should handle requests very quickly.
* Access the FastAPI health check endpoint in your browser: [http://127.0.0.1:8000/get_status](http://127.0.0.1:8000/get_status).

---

##  API Endpoints

The FastAPI application exposes the following endpoints:

### `POST /register_event`

Accepts a JSON event payload and asynchronously pushes it to the `events` Kafka topic. This endpoint is designed for speed and responsiveness.

**Request Body Example:**

# What This Project Demonstrates
This project provides a hands-on understanding of several critical concepts in modern data architecture:

Handling High-Throughput Requests: Shows how a FastAPI application can efficiently receive and queue thousands of requests per second by offloading processing.

Asynchronous Event-Driven Architecture: Illustrates the power of decoupling components using a message broker (Kafka), allowing producers and consumers to operate independently.

Kafka Integration with FastAPI: Provides a practical example of how to integrate a web API with a robust message queue for reliable data ingestion.

Decoupling Producers and Consumers: Highlights the benefits of this pattern, including improved fault tolerance, scalability, and maintainability.

Real-World Traffic Simulation: The simulate_traffic.py script mimics production-like conditions, allowing you to observe the system's performance under load.

Logging and Observability Practices: The consumer's logging mechanism demonstrates a basic form of observing processed data, crucial for debugging and monitoring.

Dockerized Microservices Setup: All core components are containerized, ensuring consistent environments and simplifying deployment across different machines.

# Learning Goals
By exploring and running this project, you will gain valuable insights into:

Scalable API Ingestion: Understanding how to design APIs that can handle a massive influx of data without becoming a bottleneck.

Event-Driven System Design: Grasping the principles of building systems where actions are triggered by events, leading to more resilient and flexible architectures.

Apache Kafka Fundamentals: Learning how Kafka acts as a central nervous system for data, enabling reliable data streaming and processing.

Distributed System Concepts: Experiencing how different services (FastAPI, Kafka, Consumer) work together in a distributed environment.

Observability in Action: Observing how logs can provide insight into the flow and processing of data within the pipeline.

# Contributing
Contributions, issues, and feature requests are welcome! If you have ideas for improvements or encounter any problems, please feel free to:

Open an issue: Describe the bug or feature request in detail.

Submit a Pull Request: If you've implemented a solution or a new feature, we'd love to see it!

# License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
The creators and maintainers of FastAPI, Apache Kafka, Zookeeper, and Docker for providing such powerful open-source tools.



