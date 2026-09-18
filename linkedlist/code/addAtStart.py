class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Existing linked list
node1 = Node(10)
node2 = Node(20)

node1.next = node2

# Insert 5 at beginning
new_node = Node(5)

new_node.next = node1
node1 = new_node

# Print linked list
current = node1

while current != None:
    print(current.data)
    current = current.next
