size = 10
table = [None] * size

def hash_function(key):
    return key % size

def insert(key, value):
    index = hash_function(key)
    table[index] = value

def get(key):
    index = hash_function(key)
    return table[index]


insert(25, "Ali")
insert(12, "Ahmed")
insert(37, "Sara")

print(get(25))
print(get(12))
print(get(37))
