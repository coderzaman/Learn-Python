# copy()
# Description: Returns a shallow copy of the set.

s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)

s2.add(4)
print(s2)

s1.add(5)
print(s1)
print(s2)