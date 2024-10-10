# Symmetric Difference (^ or .symmetric_difference())
# Description: Returns elements present in either set but not in both.

s1 = {1, 2, 3}
s2 = {3, 4, 5}

symmetric_dif = s1 ^ s2
print(symmetric_dif)

# With symmetric_difference() function
symmetric_dif = s1.symmetric_difference(s2)
print(symmetric_dif)