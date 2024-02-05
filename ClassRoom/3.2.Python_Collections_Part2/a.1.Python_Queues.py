from collections import deque

# Queue in Python using deque

queue = deque()

# Enqueuing elements to queue
queue.append('a')
queue.append('b')
queue.append('c')

# Dequeuing elements from queue
first_item = queue.popleft()

print(queue)  # Output: deque(['b', 'c'])
