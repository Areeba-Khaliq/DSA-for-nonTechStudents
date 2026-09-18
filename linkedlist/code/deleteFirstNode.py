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

# Delete first node
node1 = node1.next

# Print linked list
current = node1

while current != None:
    print(current.data)
    current = current.next
