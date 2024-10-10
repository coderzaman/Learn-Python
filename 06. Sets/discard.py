# discard()
# Description: Removes a specified element from the set if it exists. Does not raise an error if the element is not found.

s = {1, 2, 3, 4}
s.discard(3)
print(s)

print(s.discard(5))
print(s)

