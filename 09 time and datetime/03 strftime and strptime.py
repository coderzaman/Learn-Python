# Date and Time Formatting
# Formatting dates and times allows you to convert struct_time or datetime objects to strings and vice versa.

# strftime: Converts a struct_time or datetime object to a formatted string.
# strptime: Parses a string into a struct_time or datetime object based on a format.

# Using strftime
# Example: Formatting Current Local Time

import time
from datetime import datetime

current_time = time.localtime()

# print(type(current_time))

formatted_time = time.strftime("%A, %B %d, %Y %I:%M:%S %p", current_time)
print(formatted_time)


print()

# Using strptime
# Example: Parsing a Date String to struct_time
date_string = formatted_time
formated_string = "%A, %B %d, %Y %I:%M:%S %p"
passed_time = time.strptime(date_string, formated_string)
print(passed_time)

