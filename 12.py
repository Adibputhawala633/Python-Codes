#12.	Write a program to demonstrate the Dictionary function.
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("dict1 => ", dict1)

dict1["age"] = 31
dict1["country"] = "USA"
dict1["name"] = "Jane"
dict1["city"] = "Los Angeles"
dict1["hobby"] = "reading"
dict1["age"] = 32


print("dict1 => ", dict1)
print("dict1.get('name')", dict1.get("name"))
print("dict1.get('age')", dict1.get("age"))
print("dict1.get('city')", dict1.get("city"))
print("dict1.get('country')", dict1.get("country"))
print("dict1.get('hobby')", dict1.get("hobby"))

print("dict1.keys()", dict1.keys())
print("dict1.values()", dict1.values())
print("dict1.items()", dict1.items())
print("dict1.pop('age')", dict1.pop("age"))
print("dict1.popitem()", dict1.popitem())
print("dict1.clear()", dict1.clear())
print("dict1 => ", dict1)

print("dict1.setdefault('name')", dict1.setdefault("name", "John"))
print("dict1.setdefault('age')", dict1.setdefault("age", 30))


print("dict1 => ", dict1)
print("dict1.update({'name': 'Jane'})", dict1.update({"name": "Jane"}))
print("dict1 => ", dict1)