# Removing unwanted files helps in maintaining a clean file system.
import os

file_path = 'unwanted_file.txt'

try:
    os.remove(file_path)
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("Permission Denied")

print()
# Using the pathlib Module:
from pathlib import Path
file_path = Path('unwanted_file.txt')

if file_path.exists():
    file_path.unlink()
else:
    print("File Not Exist")

 # shutil.rmtree() permanently deletes the directory and all its contents. Use it carefully to avoid accidental data loss.