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


# Insert 40 at the end
new_node = Node(40)

current = node1

while current.next != None:
    current = current.next

current.next = new_node


# Print linked list
current = node1

while current != None:
    print(current.data)
    current = current.next
