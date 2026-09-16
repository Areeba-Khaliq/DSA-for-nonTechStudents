from queue import Queue

queue = Queue()

def enqueue(x):
    queue.put(x)

def dequeue():
    if queue.empty():
        print("Queue is empty")
        return None
    return queue.get()

def peek():
    if queue.empty():
        print("Queue is empty")
        return None
    return queue.queue[0]

def isEmpty():
    return queue.empty()

def size():
    return queue.qsize()

enqueue(10)
enqueue(20)
enqueue(30)

print(dequeue())   # 10
print(peek())      # 20
print(size())      # 2
print(isEmpty())   # False
