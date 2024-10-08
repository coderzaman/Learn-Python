numbers = [10, 20, 30, 40, 50]
# Change the first item
numbers[0] = 13
print(numbers)

# changing last item
numbers[-1] = 34
print(numbers)

#changing last second item
numbers[-2] = 90
print(numbers)

# Swap First and Last Item
print(numbers)
numbers[0], numbers[-1] = numbers[-1],numbers[0]
print(numbers)

numbers[-1], numbers[0] = numbers[0],numbers[-1]
print(numbers)