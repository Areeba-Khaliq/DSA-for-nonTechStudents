class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node1


# Traverse
current = node1

for i in range(6):
    print(current.data)
    current = current.next
