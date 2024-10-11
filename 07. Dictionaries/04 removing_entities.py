# Removing Entries:

# Using del: del dictionary["key]
person = {"name": "Alice", "age": 30, "profession": "Engineer"}
del person["age"]

print(person)
print()

# using .pop(item_key) // return removing item
person = {"name": "Alice", "age": 30, "profession": "Engineer"}
profession = person.pop("profession")

print(profession)
print(person)
print()

# Using .popitem():
# Removes and returns an arbitrary key-value pair (as of Python 3.7, it removes the last inserted item)
person["profession"]  = "Programmer"
print(person)

pop_item = person.popitem()
print(pop_item)
print(person)

# Clearing the Dictionary:
person.clear()
print(person)

