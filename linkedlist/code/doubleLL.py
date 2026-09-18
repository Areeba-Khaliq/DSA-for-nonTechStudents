class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2


# Traverse forward
current = node1

while current != None:
    print(current.data)
    current = current.next
