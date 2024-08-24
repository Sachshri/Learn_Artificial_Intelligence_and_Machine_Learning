#math
import math
##Arithmetic function
print(math.ceil(5.6))
print(math.floor(8.9))
print(math.trunc(8.8))

##logarithmic and exponential
print(math.log(6,2))
print(math.log(25,10))
print(math.log(8,2))

print(math.exp(6))

##trigonometric
print(math.sin(math.pi))
print(math.tan(math.radians(90)))
print(math.cos(math.degrees(math.pi/2)))

##Some constants
print(math.pi)
print(math.e)

#Random library
import random as rm
print(rm.random())
print(rm.randint(1,66))
print(rm.uniform(8.0,66.7))
lst=[6,7,8,3,0]
print(rm.choice(lst))
print(rm.sample(lst,3))
rm.shuffle(lst)
print(lst)

#DataTime
import datetime as dt

print(dt.datetime.now())
print(dt.datetime(99,8,10,9,8,5))

from datetime import datetime,timedelta
current_datetime=datetime.now()

# Format a datetime object as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Parse a string into a datetime object
parsed_date = datetime.strptime("2023-01-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_date)

current_datetime=datetime.now()
future_date = current_datetime + timedelta(days=7)
print(future_date)


#Collection
from collections import Counter,defaultdict,OrderedDict
print(Counter([9,4,7,8,3,4,6,7]))
d=defaultdict(int)
d['a']=9
d['b']=90
print(d)

d=OrderedDict()
d["Guru"]=8
d["hello"]=4
print(d)

#Strings
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)


print(2000/25)