# Using Write Mode ("w"):
# Behavior: Creates new_file.txt if it doesn't exist. If it exists, overwrite the content
with open('../file_io_test/new_file.txt', 'w') as file:
    file.write("This is a new file.")



# Using Exclusive Creation Mode ("x"):
# Behavior: Creates new_file.txt if it doesn't exist. If it exists, overwrite the content
try:
    with open('../file_io_test/exclusive_file.txt', 'x') as file:
        file.write("This file is created exclusively.")
except FileExistsError:
    print("File already exists.")

