# - or .difference()
# In set difference, we remove the elements that are common to both sets from the first set.


s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {1, 2}

difference_set = s1 - s2
print(difference_set)

print()

difference_set = s1 - s2 - s3
print(difference_set)
print()

# .difference() function
set_difference = s1.difference(s2)
print(set_difference)
print()

set_difference = s1.difference(s1,s2,s3)
print(set_difference)