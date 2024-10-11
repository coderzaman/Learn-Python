# Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.

person = {"name": "Alice", "age": 30}


person.update(
    {
        "profession": "Programmer",
        "salary": 400000,
        # If you add Existing value it will be changing existing item value
        "name" : "John"
    }
)

print(person)
print()
# You can als add a new dictionary to it
address = {"city": "Cox's Bazar", "country:": "Bangladesh"}
person.update(address)
print(person)

# You add list of tuples key value pairs to dictionary
fav = [("hobby", "Coding"), ("fav-color","Black and White")]
print(fav)


# You add list of list value pairs to dictionary
additional_inf = [["Weight", 56], ["height", 5.5], ["eye-color", "black"]]
print(additional_inf)

person.update(additional_inf)
print(person)

