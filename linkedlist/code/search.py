current = node1
found = False

while current != None:
    if current.data == 30:
        found = True
        break

    current = current.next

if found:
    print("Element found")
else:
    print("Element not found")
