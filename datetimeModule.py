import datetime
import pytz

c= datetime.datetime.now()
est = pytz.timezone('US/Eastern')
print("The current UTC datetime is", c.strftime("%m/%d/%Y, %H:%M:%S %p"))

fmt = '%Y-%m-%d %H:%M:%S %Z%z' #24 hours
fmt1= '%m/%d/%Y, %I:%M:%S %p %Z%z' #12 hours

print ("The current EST datetime in 24 hours format is ", c.astimezone(est).strftime(fmt))
print ("The current EST datetime in 12 hours format is ", c.astimezone(est).strftime(fmt1))
