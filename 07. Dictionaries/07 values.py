# Returns a view object containing all the values in the dictionary.

person = {"name": "Alice", "age": 30, "profession": "Engineer"}
p_values = person.values()
print(type(p_values))
print(p_values)


# Iterating through values
for value in p_values:
    print(value)