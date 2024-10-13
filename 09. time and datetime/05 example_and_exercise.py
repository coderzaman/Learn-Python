# Getting Current Date and Time
# using time module

import time
from os import utime

current_time = time.time()
struct_time = time.localtime(current_time)
print(struct_time)

c_time = time.ctime(current_time)
print(c_time)


# Using datetime Module:
from datetime import  datetime
current_time = datetime.now()
print(current_time.ctime())

# Formatting Dates

# Convert datetime to String:
string_time = str(datetime.now()).split('.')[0]
format_time = "%A, %B %d, %Y %I:%M:%S %p"

print()
passed_date_time = datetime.strftime(datetime.now(), format_time)
print(passed_date_time)
print(string_time)


print()
passed_date_time = datetime.strptime("Sunday, October 13, 2024 01:13:20 PM", "%A, %B %d, %Y %I:%M:%S %p")
print(type(passed_date_time))



print()


local_time = time.localtime()
formatted_time = time.strftime(format_time, local_time)
print(formatted_time, type(formatted_time))

# Example 3: Parsing Strings to Dates
# Parse String to datetime Object:
string_time = str(datetime.now()).split(".")[0]

passed_date_time = datetime.strptime(string_time, "%Y-%m-%d %H:%M:%S")
# print(type(passed_date_time))



date_string = "Monday, October 08, 2024"
format_string = "%A, %B %d, %Y"

parsed_time = time.strptime(date_string, format_string)
print(parsed_time)

print()
# Example 4: Calculating Time Differences
# Using datetime:
from datetime import datetime

#Define tow dates
# Using datetime:
# Calculate age
birdate = datetime(1998, 4, 13)
print(datetime.now()- birdate)


# or using  relativedelta
from datetime import datetime
from dateutil.relativedelta import relativedelta

birthdate = datetime(1998, 4, 13)
now = datetime.now()

difference = relativedelta(now, birthdate)

print(f"{difference.years} years, {difference.months} months, and {difference.days} days")

print("\nExercise:")

# Exercise 1: Current Time in Different Formats
# Task: Write a Python script that prints the current date and time in the following formats:
#
# YYYY-MM-DD HH:MM:SS
# Day, Month DD, YYYY
# MM/DD/YYYY
# HH:MM AM/PM

today = datetime.now()

print(datetime.strftime(today, "%Y-%m-%d %H:%M:S"))
print(datetime.strftime(today, "%A, %B %d, %Y"))
print(datetime.strftime(today, "%m/%d/%Y"))
print(datetime.strftime(today, "%H:%M:%S %p"))

# Exercise 2: Calculate Days Until New Year
# Task: Write a Python program that calculates the number of days remaining until January 1st of the next year.

def days_until_new_year():
    today = datetime.now()
    new_year = datetime(today.year+1,1,1)
    days_remain = new_year - today
    return days_remain.days


print("Days Until New Year is: ", days_until_new_year())

print()
# Parse and Format Date from User Input
# Task: Prompt the user to enter a date in the format DD-MM-YYYY, parse it into a datetime object, and then print it in the format Month DD, YYYY.
#

# date_input = input("Please Enter a date (DD-MM-YYYY): ")
#
# input_format = "%d-%m-%Y"
# output_format = "%B %d, %Y"
#
# try:
#     input_format = datetime.strptime(date_input, input_format)
#     output_format = datetime.strftime(input_format, output_format)
#     print(output_format)
# except ValueError:
#     print("Invalid date format. Please use DD-MM-YYYY.")
#

print()

# # Exercise 4: Timezone Conversion
# # Task: Write a Python script that gets the current UTC time and converts it to Eastern Standard Time (EST).

from datetime import timezone, timedelta
utc_time = datetime.now(timezone.utc)
print(utc_time)

# Define BDT timezone BDT UTC(+6)
bdt = timezone(timedelta(hours=6))

#comvert utc to BDT
bdt_time = utc_time.now(bdt)
print("BDT Time is:", bdt_time.strftime("%B, %m %A, %Y %I:%M:%S %p"))

from dateutil.relativedelta import relativedelta
# Exercise 5: Calculate Age from Birthdate
# Task: Write a Python program that prompts the user to enter their birthdate in YYYY-MM-DD format and calculates their age in years.
# from datetime import datetime

# def calculate_age(birthdate_str):
#     format_str = "%Y-%m-%d"
#
#     try:
#         today = datetime.now()
#         birth_date = datetime.strptime(birthdate_str, format_str)
#         calculate_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.year))
#         return calculate_age
#     except ValueError:
#         print("Invalid Date formant. Please Provide date to this format:  YYYY-MM-DD")
#
#
# # Prompt user for input
# birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
# age = calculate_age(birthdate_input)
# print("Your Age:", age)


# Second Way relativedelta

def calculate_age(birth_str):
    date_formats = "%Y-%m-%d"
    try:
        birth_date = datetime.strptime(birth_str, date_formats)
        today_date = datetime.now()
        difference = relativedelta(today_date, birth_date)
        return difference
    except ValueError:
        print("Invalid Date formant. Please Provide date to this format:  YYYY-MM-DD")

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate_input)
print(f"Your Age is: {age.years} years, {age.months} months, and {age.days} days")

