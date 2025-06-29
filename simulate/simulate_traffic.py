# simulate_traffic.py

import requests
import random
import string
import time

URL = "http://localhost:8000/register_event"

def random_event():
    return {
        "event_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        "event_type": random.choice(["click", "view", "purchase", "logout"]),
        "payload": {
            "user_id": f"user_{random.randint(1, 100)}",
            "action": random.choice(["open_app", "click_button", "scroll", "exit"])
        }
    }

def simulate_requests(n=10000, delay=0.01):
    start = time.time()
    success = 0
    for _ in range(n):
        data = random_event()
        response = requests.post(URL, json=data)
        if response.status_code == 200:
            success += 1
        time.sleep(delay)  # Small delay to avoid overwhelming the server
    end = time.time()
    print(f"Sent {success} successful requests out of {n} in {end - start:.2f} seconds")

if __name__ == "__main__":
    simulate_requests()


######## empty traffic ######

# import requests
# import random
# import time
# from concurrent.futures import ThreadPoolExecutor

# URL = "http://localhost:8000/register_event"

# def send_request(i):
#     payload = {"user_id": i, "event": "click", "fail": random.choice([False, False, True])}
#     try:
#         requests.post(URL, json=payload)
#     except Exception as e:
#         print(f"Request {i} failed: {e}")

# if __name__ == "__main__":
#     start = time.time()
#     with ThreadPoolExecutor(max_workers=100) as executor:
#         for i in range(10000):
#             executor.submit(send_request, i)
#     print(f"Sent 10,000 requests in {time.time() - start:.2f} seconds")
