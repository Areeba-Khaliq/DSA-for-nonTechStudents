class Queue:
    def __init__(self):
        self.queue = []

    # Add item at the rear
    def enqueue(self, x):
        self.queue.append(x)

    # Remove and return the front item
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        return self.queue.pop(0)

    # Return the front item without removing it
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None

        return self.queue[0]

    # Check whether queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # Return number of items
    def size(self):
        return len(self.queue)

  q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.queue)

print(q.dequeue())
print(q.peek())
print(q.isEmpty())
print(q.size())
