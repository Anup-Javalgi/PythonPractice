# Date Time modules in Python

import datetime

date = datetime.date(2025, 1, 2)
print(date)

today =  datetime.date.today()
print(today)

time = datetime.time(12, 30, 0)
print(time)

now = datetime.datetime.now()
print(now)

now = now.strftime("%H : %M : %S  %d %m %Y")
print(now)

target_datetime = datetime.datetime(2025, 1, 2, 11, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print(f"{target_datetime} has passed {current_datetime}")
else:
    print(f"{target_datetime} has not passed {current_datetime}")