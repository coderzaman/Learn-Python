# FileNotFoundError	Raised when a file or directory is not found.
# PermissionError	Raised when the operation lacks the necessary permissions.
# IsADirectoryError	Raised when a directory operation is requested on a non-directory.
# EOFError	Raised when the end-of-file condition is reached.
# IOError	General I/O related errors. (In Python 3.x, IOError is an alias for OSError.)

# Handling File Not Found
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")


# Example: Handling Permission Denied
try:
    with open('/root/secret_file.txt', 'r') as file:
        content = file.read()
except PermissionError:
    print("You do not have permission to read this file.")

# General Exception Handling
# While it's good practice to handle specific exceptions, you can also catch general exceptions to prevent your program from crashing unexpectedly.

try:
    with open('example.txt', 'r') as file:
        content = file.read()
except Exception as e:
    print(f"An error occurred: {e}")

# Note: Avoid using bare except: clauses as they can catch unexpected exceptions, making debugging harder.
