# pop(): Removes the specified key and returns its value. If the key is not found, it raises a KeyError unless a default value is provided.

person = {"name": "Alice", "age": 30, "profession": "Engineer"}

# Popping an existing key
profession = person.pop("profession")
print(profession)  # Output: Engineer
print(person)      # Output: {'name': 'Alice', 'age': 30}

# Popping a non-existent key without default (Raises KeyError)
# salary = person.pop("salary")  # Raises KeyError: 'salary'

# Popping a non-existent key with default
salary = person.pop("salary", 50000)
print(salary)  # Output: 50000
print(person)  # Output: {'name': 'Alice', 'age': 30}
