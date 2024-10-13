# Building datetime Objects from Formatted Strings
# While the time module offers basic functionality, the datetime module provides a more intuitive and feature-rich way to handle dates and times.

# Parsing Strings to datetime Objects with strptime
# Importing datetime

from  datetime import datetime
from os import utime
from venv import create

datetime_string = str(datetime.now())
format_string = "%Y-%m-%d %H:%M:%S.%f"

parsed_date = datetime.strptime(datetime_string, format_string)
print(parsed_date.date())
print(parsed_date.time())


datetime_string = str(datetime.now()).split(".")[0]
format_string = "%Y-%m-%d %H:%M:%S"
passed_datetime = datetime.strptime(datetime_string, format_string)
print(passed_datetime)

# strftime: Converts a struct_time or datetime object to a formatted string.
datetime_object = datetime.now()
format_string = "%A, %B %d, %Y %I:%M:%S %p"

passed_datetime = datetime.strftime(datetime_object, format_string)
print(passed_datetime)

# datetime Objects from Components
custom_datetime = datetime(2024, 10, 13, 12,45,00,00)
print(custom_datetime)

# Handling Time Zones with datetime
# Python's datetime module also supports timezone-aware objects using the timezone class or third-party libraries like pytz

from datetime import datetime, timezone, timedelta

#current UTC time
utc_now = datetime.now(timezone.utc)
print(utc_now)

# create timezone from UTC+6
tz_plus_6 = datetime.now(timezone(timedelta(hours=6)))
print(tz_plus_6)

# 