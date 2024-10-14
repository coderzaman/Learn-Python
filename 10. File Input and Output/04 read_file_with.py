# When we with file with statement it does not need to close manually

# Reading the Entire File:
with open('../file_io_test/one.txt', 'r') as file:
    content = file.read()
    print(content)

print()
# Reading Specific Number of Characters:
with open('../file_io_test/one.txt', 'r') as file:
    content = file.read(10)
    print(content)

print()
# Reading Lines into a List:
with open('../file_io_test/one.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

print()

# Iterating Over Each Line:(Reading Files Line by Line)
with open('../file_io_test/one.txt', 'r') as file:
    for line in file:
        print(line.strip())

