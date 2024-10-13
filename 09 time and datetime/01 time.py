import time
# time() return number of second passed since epoc
# epoc: Time passed since January 1, 1970
seconds =  time.time()

# The time.ctime() take no seconds and return a string representing local time base on seconds
print(time.ctime(seconds))
print(time.ctime(1000000000))


#time.sleep() suspend number of seconds current thread
print("Ha Ha!")
time.sleep(.5)
print("Ha Ha " * 3)

# time.localtime() function take the no of seconds as argument and returns struct_time(a tuple contain 9 element corresponding to struct_time)
print(time.localtime(seconds))
print(time.localtime(1000000000))

# DateTime
# DataTime module provides a variety of classes for representing and manipulating dates and times, as well as for formatting and parsing dates and times in various of formats

import datetime

# print current datetime with with datetime.now(). datetime is class of datetime module. It provides local time
print(datetime.datetime.now())

# current utc time
print(datetime.datetime.utcnow())

# get today with date.today() function. Here date is a class and today() is function of it
print(datetime.date.today())

# get date, time, year, month form fromtimestamp(seconds) function of date class
random_time = datetime.date.fromtimestamp(100000000)
print(type(random_time))

print(random_time.day)
print(random_time.year)
print(random_time.month)


