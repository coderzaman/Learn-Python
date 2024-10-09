# Syntax
# while condition:
    # Code block to execute repeatedly

# Example
count = 0

while count < 5:
    print(count)
    count += 1  # Increment count to eventually break the loop

print()
# Nested while Loops
# print 1 to 10 multiplication table

i = j = 1

while i <= 10:

    while j <= 10:
        print(f'{i} * {j} = {i*j}')
        j = j+1
    i= i+1
    j = 1
    print()

