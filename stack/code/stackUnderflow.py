class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Underflow")

    # size
    def size(self):
        return len(self.stack)

    # isEmpty
    def isEmpty(self):
        return len(self.stack) == 0

    # top
    def top(self):
        return self.stack[-1]


s = Stack()

s.push(10)
s.push(20)

print(s.stack)
print(s.pop())
print(s.top())
print(s.size())
print(s.isEmpty())
