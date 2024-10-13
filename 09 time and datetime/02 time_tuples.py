# A time tuple(struct_time) is a named tuple that represents a specific moment in time. It's returned by several functions in the time module.

# The struct_time tuple has the following attributes:
# tm_year	Year (e.g., 2024)
# tm_mon	Month (1-12)
# tm_mday	Day of the month (1-31)
# tm_hour	Hour (0-23)
# tm_min	Minute (0-59)
# tm_sec	Second (0-60, allowing for leap seconds)
# tm_wday	Day of the week (0-6, Monday is 0)
# tm_yday	Day of the year (1-366)
# tm_isdst	Daylight Saving Time flag (-1, 0, 1)

# Creating and Accessing struct_time

import time
from datetime import datetime


# Get the current local time as a struct_time
current_time = time.localtime()
print(current_time)
print()
# Access Individual Attribute
print("Date: ", current_time.tm_mday)
print("Month: ", current_time.tm_mon)
print("Month: ", current_time.tm_year)
print("Hours: ", current_time.tm_hour)
print("Minutes:", current_time.tm_min)
print("Seconds: ", current_time.tm_sec)
print("Daylight Saving Time:", current_time.tm_isdst)
print()
# tm_isdst: Daylight Saving Time is in effect
# Daylight Saving Time (DST) is when clocks are set forward by one hour during the warmer months to make better use of daylight.
# Typically, clocks are moved forward one hour in the spring ("spring forward") and moved back one hour in the fall ("fall back").

# Common time Module Functions Returning struct_time
# time.localtime([secs]): Converts seconds since the epoch to struct_time in local time.
# time.gmtime([secs]): Converts seconds since the epoch to struct_time in UTC.
# time.strptime(string, format): Parses a string into struct_time based on the specified format.

print(time.localtime())
print(time.gmtime())
print()





date_string = str(datetime.now()) # print current date and this format: 2024-10-13 00:06:53.651248
print(type(date_string))
date_format = "%Y-%m-%d %H:%M:%S.%f"
parsed_time = time.strptime(date_string, date_format)
print(parsed_time)

date_string = str(datetime.now())
date_format = "%Y-%m-%d %H:%M:%S"
parsed_time = time.strptime(date_string.split(".")[0], date_format)
print(parsed_time)