# Writing to Files
# Opening a file in write mode ("w") overwrites the existing content
# If file is not exist create file first then write data
from Cryptodome.SelfTest.Cipher.test_CBC import file_name
from Cryptodome.Util.RFC1751 import binary

with open('../file_io_test/example.txt', 'w') as file:
    file.write("This will overwrite existing content.")

# Appending to a File:
# Opening a file in append mode ("a") adds content to the end without altering existing data.
with open('../file_io_test/example.txt', 'a') as file:
    file.write("\nNew Line Append.")


# Writing Multiple Lines:
lines = ["First line.\n", "Second line.\n", "Third line.\n"]

with open('../file_io_test/example.txt', 'w') as file:
    file.writelines(lines)

# Append Multiple Line
lines = ["\nFourth line.\n", "Five line.\n", "Six line.\n"]

with open('../file_io_test/example.txt', 'a') as file:
    file.writelines(lines)

