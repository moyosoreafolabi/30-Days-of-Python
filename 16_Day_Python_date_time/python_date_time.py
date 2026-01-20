import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

# formatting the date time using strftime method 

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40

from datetime import date
d = date(2026, 1, 19)
print(d)       
print('Current date:', d.today())  
# date object of today's date
today = date.today()
print("Current year:", today.year)   
print("Current month:", today.month) 
print("Current day:", today.day)    

# time objects to represent time

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555

# difference between two points in time 

from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# difference between two points in time using timedelta

from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

# exercises
from datetime import datetime
now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') 

from datetime import datetime

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)

time_difference = new_year - now

days = time_difference.days
seconds = time_difference.seconds
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Time until New Year: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
# Output will vary depending on the current date and time

from datetime import datetime

epoch = datetime(1970, 1, 1)
now = datetime.now()

time_difference = now - epoch

days = time_difference.days
seconds = time_difference.seconds
years = days // 365
hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Time since 1 Jan 1970:")
print(f"{years} years, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

def nl():
    print("\n")
nl()

from datetime import datetime

time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y")

print(time_object)
# Output: 2019-12-05 00:00:00