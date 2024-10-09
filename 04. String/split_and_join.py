# Using split()
from os.path import split

s = "apple,banana,cherry"
print(s.split(","))

s = "apple banana cherry"
print(s.split(" "))

# Using join()
split_list = s.split(" ")
print(split_list)

# Return a string
joined_list = ", ".join(split_list)
print(joined_list)

