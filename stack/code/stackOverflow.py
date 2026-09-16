stack = []
max_size = 3

def push(data):
    if len(stack) == max_size:
        print("Stack Overflow")
    else:
        stack.append(data)
        print(data, "pushed")

push(10)
push(20)
push(30)
push(40)

print("Stack:", stack)
