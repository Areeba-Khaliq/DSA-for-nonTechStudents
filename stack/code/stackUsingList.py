stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# Pop
print("Popped:", stack.pop())

# Peek
print("Top element:", stack[-1])

# Size
print("Size:", len(stack))

# Empty
print("Is stack empty?", len(stack) == 0)
