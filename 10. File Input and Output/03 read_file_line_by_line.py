file = open('../file_io_test/one.txt')

while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')

file.close()

print()
print()

# Or Use
file = open('../file_io_test/one.txt')

for line in file:
    print(line,end='')

print()
print()

# We can also use readlines() method which return a list of line
file = open('../file_io_test/one.txt')
lines = file.readlines()

[print(line, end='') for line in lines]

# After perform operation with file we must need to close this file for prevent further error
