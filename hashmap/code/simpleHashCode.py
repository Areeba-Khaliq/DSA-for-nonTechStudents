class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]


ht = HashTable(10)

ht.insert(25, "Ali")
ht.insert(12, "Ahmed")
ht.insert(37, "Sara")

print(ht.get(25))
print(ht.get(12))
