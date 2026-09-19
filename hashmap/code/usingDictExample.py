hashmap = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore",
    "marks": 85
}

def get(key):
    if key in hashmap:
        return hashmap[key]
    else:
        return "Key not found"


def put(key, value):
    hashmap[key] = value


def remove(key):
    if key in hashmap:
        del hashmap[key]


print(get("name"))
print(get("marks"))

put("grade", "A")
print(hashmap)

remove("age")
print(hashmap)
