
## Q1. Queue Using List
Implement a queue using a Python list with the following functions:
enqueue()
dequeue()
peek()
isEmpty()
size()
Test your queue with:
10, 20, 30, 40
Perform two dequeue() operations and display the final queue.
## Q2. Queue Using deque
Using collections.deque, implement a queue with the following functions:
enqueue()
dequeue()
peek()
isEmpty()
size()
Your program should also handle the case when dequeue() is called on an empty queue.
## Q3. Bounded Queue
Using Python's queue.Queue, create a queue with:
maxsize = 5
Write a program that:
Adds 5 elements.
Checks whether the queue is full.
Attempts to add another element.
Removes two elements.
Adds two more elements.
Displays the size of the queue.
## Q4. Hospital Emergency Queue
Use Python's PriorityQueue to create a hospital emergency queue.
Add the following patients:
Patient A → Priority 3
Patient B → Priority 1
Patient C → Priority 2
Patient D → Priority 1
Process all patients and display the order in which they are treated.
Question: Why doesn't the queue follow the normal FIFO order?
Circular Queue — Conceptual Questions
Assume a Circular Queue of size 4 for Questions 1–8.
## Q5. The following operations are performed:
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
What will be the output of dequeue()?
What will be the values of front and rear after the operation?
## Q6. A circular queue has size 4.
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
dequeue()
Answer:
What elements are currently in the queue?
What is the value of front?
What is the value of rear?
## Q7. Full Queue
A circular queue has size 4.
enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
Now:
enqueue(50)
What will happen?
Explain why 50 cannot be inserted even though the rear can wrap around to index 0.
## Q8. Trace the Queue
A circular queue has size 4.
Perform the following operations one by one:
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
dequeue()
enqueue(50)
enqueue(60)
After every operation, write:
Array:
Front:
Rear:

