import threading
import time

# A simple function for the thread to execute
def print_numbers():
    for i in range(1, 6):
        time.sleep(1)
        print(f"Number: {i}")

# A thread worker function demonstrating a potential race condition
def increment_counter(shared_counter, lock):
    with lock:
        current_value = shared_counter[0]
        time.sleep(0.1)  # Simulating some processing
        shared_counter[0] = current_value + 1

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start threads
thread1.start()
thread2.start()

# Join threads
thread1.join()
thread2.join()

# Handling race conditions with locks
counter = [0]  # A shared resource
lock = threading.Lock()

# Create multiple threads for incrementing the counter
threads = [threading.Thread(target=increment_counter, args=(counter, lock)) for _ in range(10)]

# Start all threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final counter value: {counter[0]}")

# Demonstration of daemon threads
def daemon_worker():
    print("Starting daemon worker")
    time.sleep(2)
    print("Exiting daemon worker")

daemon_thread = threading.Thread(target=daemon_worker)
daemon_thread.setDaemon(True)
daemon_thread.start()

print("Main thread is exiting")


import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor

# Function to demonstrate thread communication
def producer(q):
    for i in range(5):
        time.sleep(1)
        print(f"Putting item {i} in the queue")
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break  # Exit condition
        print(f"Processing item {item} from the queue")
        q.task_done()

# Handling exceptions in threads
def thread_function(name):
    try:
        if name == 1:
            raise ValueError("Example exception")
        print(f"Thread {name} is running")
    except ValueError as e:
        print(f"Exception in thread {name}: {e}")

# Using a thread pool
def task(n):
    print(f"Processing task {n}")
    time.sleep(2)
    return f"Task {n} completed"

# Create a queue for thread communication
q = queue.Queue()

# Start producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

# Add None to the queue to signal the consumer to exit
q.put(None)

producer_thread.join()
consumer_thread.join()

# Handling exceptions in threads
threads = [threading.Thread(target=thread_function, args=(i,)) for i in range(3)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

# Using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, range(5))

print("All tasks complete:")
for result in results:
    print(result)

print("Main thread is exiting")
