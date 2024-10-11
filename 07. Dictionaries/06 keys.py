# Description: Returns a view object containing all the keys in the dictionary.
person = {"name": "Alice", "age": 30, "profession": "Engineer"}
keys = person.keys()
print(type(dict))
print(keys)

# Iterating through keys
for key in keys:
    print(key)

print()
#Acce value with key
for key in keys:
    print(f'{person[key]}')

