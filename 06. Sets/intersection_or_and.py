# Returns elements common to both sets.
s1 = {1, 2, 3, 5}
s2 = {3, 4, 5}
s3 = {5, 7, 8, 5, 4}

# First Intersection (s1 & s2) = {3, 5}
# Second Intersection ({3, 5} & s3): = {5}

intersection_set = s1 & s2 & s3
print(intersection_set)
# intersection()
s4 = {1,2}
intersection_set= s1.intersection(s2,s3,s4)
print(intersection_set)




