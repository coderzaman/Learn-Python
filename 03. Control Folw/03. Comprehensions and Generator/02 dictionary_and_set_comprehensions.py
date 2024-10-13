# Dictionary and Set Comprehensions
# Similar to list comprehensions, Python also supports comprehensions for dictionaries and sets.

# Dictionary Comprehension
squares_dict = {x: x**2 for x in range(1,11)}
print(squares_dict)

for key, value in squares_dict.items():
    print(f'Key: {key}, Value: {value}')

print()
# Set Comprehension
# Creating a set of unique squares
squares_set = {x**2 for x in [2,2,4,4,3,7,9,9]}
print(squares_set)
