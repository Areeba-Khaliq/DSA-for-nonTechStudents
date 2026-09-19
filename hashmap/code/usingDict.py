hashmap = {}


def put(key, value):
    hashmap[key] = value


def get(key):
    return hashmap.get(key)


def remove(key):
    if key in hashmap:
        del hashmap[key]


put("name", "Ali")
put("age", 20)
put("city", "Lahore")

print(get("name"))
print(get("age"))

remove("age")

print(hashmap)
