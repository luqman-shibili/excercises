#implementation of queue
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueue:", queue)

print("Dequeued element:", queue.popleft())
print("Queue after dequeue:", queue)