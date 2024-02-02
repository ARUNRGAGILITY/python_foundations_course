import threading
import time

def print_numbers():
    for i in range(1, 6):
        time.sleep(1)  # Simulating a task that takes some time
        print(i)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        time.sleep(1.5)
        print(letter)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Joining threads to wait for their completion
thread1.join()
thread2.join()

print("Threads finished execution")
