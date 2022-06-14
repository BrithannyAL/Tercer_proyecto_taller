import time
from datetime import datetime, timedelta

x = True
n = 5
while x == True:
    hora = time.strftime('%H:%M:%S', time.localtime())
    menoscinco = hora - timedelta(minutes=n)
    print(menoscinco)
    print(hora)
    time.sleep(5)


from datetime import datetime
from datetime import timedelta
# Get current time in local timezone
current_time = datetime.now()
print('Current timestamp: ', current_time)
n = 5
# Add 2 minutes to datetime object containing current time
future_time = current_time - timedelta(minutes=n)
print('Future Time (2 minutes from now ): ', future_time)
# Convert datetime object to string in specific format 
future_time_str = future_time.strftime('%H:%M:%S')
print('Future Time as string object: ', future_time_str)