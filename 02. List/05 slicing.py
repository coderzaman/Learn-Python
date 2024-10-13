# Slicing allows you to access a subset of a list by specifying a range of indices. The syntax uses the colon : operator.

# Syntax
# subset = my_list[start:stop:step]
# start: Starting index (inclusive). Defaults to 0 if omitted.
# stop: Ending index (exclusive). Defaults to the end of the list if omitted.
# step: Step size. Defaults to 1 if omitted.

# Examples:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index 0 to 3
print(numbers[0:4])

#index 2 to 5
print(numbers[2:6])


#index 3:last
print(numbers[3:])

#index 0 to 5
print(numbers[:6])

# index 1 to last with skip 1 step
print(numbers[1::2])


#reverse list with slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[-1::-1])
print(numbers[len(numbers)-1::-1])
print(numbers[::1])
# Important Note
# //print(numbers[-1 or 9 is same ::-1])
#
# in stop: -1 (If I put it, Python Thinking the last element =-1)
# So It print: []
#
#  start: -1[inclusive]
#  end: -1 [execlusive]
#
#  There is nothing; that's why it print []
#
#  But when python places it as default, it add memory address before 9, 8, 0,.. -1
# len(list) - 1 (or -1)
