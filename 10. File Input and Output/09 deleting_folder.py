# Removing directories (folders) can be straightforward or require caution, especially if the directory contains files.

# Deleting an Empty Directory
# Using the os Module:
import os

folder_path = '../file_io_test/folder 1'

try:
    os.rmdir(folder_path)
    print(f'{folder_path} has been deleted')
except FileNotFoundError:
    print("Folder Not Found")
except OSError:
    print("Folder Not Empty or Can not be deleted")

print()

folder_path = '../file_io_test/folder 2'

try:
    os.rmdir(folder_path)
    print(f'{folder_path} has been deleted')
except FileNotFoundError:
    print("Folder Not Found")
except OSError:
    print("Folder Not Empty or Can not be deleted")

print()

# Using the pathlib Module:
from pathlib import Path
folder_path = Path('../file_io_test/folder 1')

try:
    folder_path.rmdir()
    print(f"{folder_path} has been deleted.")
except FileNotFoundError:
    print("Folder does not exist.")
except OSError:
    print("Folder is not empty or cannot be deleted.")


# Deleting a Non-Empty Directory
import shutil

folder_path = '../file_io_test/folder 2'

try:
    shutil.rmtree(folder_path)
    print(f"{folder_path.split('/')[-1]} has been deleted successfully")
except FileNotFoundError:
    print("Folder Does not exit")
except PermissionError:
    print("Permission Denied")
