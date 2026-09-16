class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        # Queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return

        # First element
        if self.front == -1:
            self.front = 0

        # Move rear circularly
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        # Queue is empty
        if self.front == -1:
            print("Queue is empty")
            return

        data = self.queue[self.front]
        self.queue[self.front] = None

        # Only one element was present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return data

    def display(self):
        print(self.queue)
