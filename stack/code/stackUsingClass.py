class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Stack:", s.stack)

print("Popped:", s.pop())

print("Top element:", s.peek())

print("Size:", s.size())

print("Is stack empty?", s.is_empty())
