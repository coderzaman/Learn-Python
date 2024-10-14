# Using the os Module

import os
file_pah = '../file_io_test'
file_dir = os.listdir(file_pah)

# file and folder in directory
print(file_dir)

print()
# Filter file from directory
for file in file_dir:
    if os.path.isfile(os.path.join(file_pah,file)):
        print(file)
print()
# Filter file and crate list
file_list = [file for file in file_dir if os.path.isfile(os.path.join(file_pah, file))]
print(file_list)

print()
# or print file list
[print(file) for file in file_dir if os.path.isfile(os.path.join(file_pah, file))]
print()


# Using the os.scandir() Method. It return posix.ScandirIterator object
file_dir = os.scandir(file_pah)

for file in file_dir:
    #file.name give the file name
    print(file.name)

#separator
print()

# filter file from directory. This loop is not work because os.scandir() method return an iterable.
# Iterable behaviour is if You fully it there no more item exist

for file in file_dir:
    if file.is_file():
        print(file.name)



#  If you encounter the problem convert it to list
file_dir = list(os.scandir(file_pah))

for file in file_dir:
    print(file)


print()

# Print only file
file_list = [file.name for file in file_dir if file.is_file()]
print(file_list)
print()
[print(file.name) for file in file_dir if file.is_file()]

print()

# using pathlib module Path class
from pathlib import Path

file_dir = Path(file_pah).iterdir() #it returns a generator object Path.iterdir
print(file_dir)

print()
for file in file_dir:
    print(file.name)

print()

# this loop does not print anything because of file_dir is a generator
for file in file_dir:
    print(file.name)

print()

# If we terminate this problem we can convert list to it then use it
file_dir = list(Path(file_pah).iterdir())

for file in file_dir:
    print(file.name)

print()
# filter File name
file_list = [file.name for file in file_dir if file.is_file()]
print(file_list)

print()
[print(file.name) for file in file_dir if file.is_file()]