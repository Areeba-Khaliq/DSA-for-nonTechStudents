size = 5
table = [None] * size


def hash_function(key):
    return key % size


def insert(key, value):
    index = hash_function(key)

    while table[index] is not None:
        index = (index + 1) % size

    table[index] = (key, value)


insert(10, "Ali")
insert(15, "Ahmed")

print(table)
