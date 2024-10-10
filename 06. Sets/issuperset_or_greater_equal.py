# Superset (>= or .issuperset())
# Description: Checks if a set contains all elements of another set.

s1 = {1, 2, 3}
s2 = {1, 2}

# Using >= operator
is_superset = s1 >= s2
print(is_superset)  # Output: True

# Using .issuperset() method
is_superset = s1.issuperset(s2)
print(is_superset)  # Output: True

print(s2.issuperset(s1))