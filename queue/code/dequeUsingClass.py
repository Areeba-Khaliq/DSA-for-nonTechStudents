from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            print("Queue is empty")

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty")

    def display(self):
        print(self.queue)
