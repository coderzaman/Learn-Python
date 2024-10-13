
# Description: Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
s = {1, 2, 3}
element = s.pop()
print(element)  # Output: 1 (could be any element)
print(s)        # Output: {2, 3} (assuming 1 was popped)

# Note: Since sets are unordered, pop() does not guarantee which element will be removed.