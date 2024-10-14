# Exercise 1: Counting Lines in a File
# Task: Write a Python script that counts the number of lines in a given text file one.txt

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print("File not found.")
        return 0

# Usage
line_count = count_lines('../file_io_test/one.txt')
print(f"Number of lines: {line_count}")

print()
# Exercise 2: Copying a File
# Task: Write a Python function that copies the contents of source.txt to destination.txt.
import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}.")
    except FileNotFoundError:
        print("Source file does not exist.")
    except PermissionError:
        print("Permission denied.")

# Usage
copy_file('../file_io_test/source.txt', '../file_io_test/destination.txt')
