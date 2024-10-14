# Before performing operations like reading or writing, it's often necessary to check if a file exists.
# Using the os Module:

import os

file_path = '../file_io_test/example.txt'

if os.path.isfile(file_path):
    print("File is Exist")
else:
    print("File is not exist")

print()

file_path = 'example.txt'

if os.path.isfile(file_path):
    print("File is Exist")
else:
    print("File is not exist")

print()


# os.path.exists() returns True for both files and directories. To check specifically for files:
folder_path = '../file_io_test'

if os.path.exists(folder_path):
    print("Directories is Exist")
else:
    print("Directories is not Exist")

print()


# Using the pathlib Module:

from pathlib import Path

file_path = Path('../file_io_test/new_file.txt')

if file_path.is_file():
    print("Exist")
else:
    print("Not Exist")

print()

file_path = Path('new_file.txt')

if file_path.is_file():
    print("Exist")
else:
    print("Not Exist")


#checking folder
# is_dir() method use for return directory
print()
file_path = Path('../file_io_test')

if file_path.is_dir():
    print("Exist")
else:
    print("Not Exist")

print()

# or use exists() check both file and directory exist
file_path = Path('file_io_test')

if file_path.exists():
    print("Exist")
else:
    print("Not Exist")

print()
