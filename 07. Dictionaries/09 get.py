# Returns the value for a specified key if the key exists; otherwise, returns None or a specified default value.

person = {"name": "Alice", "age": 30}
name = person.get("name")
print(name)

# Non-existent key return the none
salary = person.get("salary")
print(salary)

# you can replace the null with other value
print(person.get(salary, 5000000))
print(person.get("occupation", "Programmer"))