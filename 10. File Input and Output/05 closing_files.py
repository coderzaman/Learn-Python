# Properly closing files ensures that resources are freed and data is correctly written to disk.
file = open('../file_io_test/one.txt', 'r')
content = file.read()
print(content)
file.close()

print()

# Automatic Closing with Context Managers:
# As shown earlier, using with ensures automatic closing.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed here


# Recommendation: Always use context managers to handle files. It reduces the risk of forgetting to close files and manages exceptions gracefully.

