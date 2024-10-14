
# Example 1: Reading a Configuration File
# Scenario: You have a configuration file config.txt containing key-value pairs.

import os



file_path = '../file_io_test/config.txt'
config = {}
if os.path.isfile(file_path):
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=',1)
                config[key.strip()] = value.strip()
else:
    print(f"{file_path.split('/')[0]} Not Found")

print(config)


# Example 2: Logging Events to a File
# Scenario: You want to log application events with timestamps.

from datetime import datetime

def log_event(message, log_file='../file_io_test/app.log'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"
    with open(log_file, 'a') as file:
        file.write(entry)

# Usage
log_event("Application started.")
log_event("User logged in.")

print()
# Example 3: Processing a CSV File
# Scenario: You have a CSV file data.csv and want to process its contents.
import csv

with open('../file_io_test/data.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row['Name']
        age = int(row['Age'])
        country = row['Country']
        print(f"{name} is {age} years old and lives in {country}.")

print()
# Example 4: Creating and Writing to a New File
# Scenario: You want to create a new file report.txt and write a summary.
summary = """
Report Summary
--------------
Total Users: 150
Active Users: 120
New Signups Today: 5
"""

with open('../file_io_test/report.txt', 'w') as file:
    file.write(summary)

print("Report created successfully.")

print()
# Example 5: Deleting a Temporary File
# Scenario: After processing, you want to delete a temporary file temp_data.txt.
import os

temp_file = 'temp_data.txt'

if os.path.exists(temp_file):
    try:
        os.remove(temp_file)
        print(f"{temp_file} has been deleted.")
    except PermissionError:
        print("Permission denied. Cannot delete the file.")
else:
    print("Temporary file does not exist.")


