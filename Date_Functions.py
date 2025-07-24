import datetime
from time import strftime

curr_date = datetime.datetime.now()
print("current timestamp    : ",curr_date)
print("current year         : ",curr_date.year)
print("current month        : ",curr_date.month)
print("current day          : ",curr_date.day)
print("current hour         : ",curr_date.hour)
print("current minute       : ",curr_date.minute)
print("current second       : ",curr_date.second)

print(curr_date.date())
print(curr_date.time())
print(strftime("%X"))












