# setdefault(): Returns the value of a key if it exists; otherwise, inserts the key with a specified default value and returns that value.
person = {"name": "Alice", "age": 30}

# Existing key
name = person.setdefault("name", "Unknown")
print(name)
print(person)

# Non-existent key
salary = person.setdefault("salary", 400000)
print(salary)
print(person)