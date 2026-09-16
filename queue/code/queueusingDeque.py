from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Dequeue
print(queue.popleft())

print(queue)
