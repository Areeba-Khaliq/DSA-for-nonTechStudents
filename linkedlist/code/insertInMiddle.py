class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4


# Insert 25 after 20
new_node = Node(25)

current = node1

while current.data != 20:
    current = current.next

new_node.next = current.next
current.next = new_node


# Print linked list
current = node1

while current != None:
    print(current.data)
    current = current.next
