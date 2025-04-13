# count down time in python

import time

countdown = int(input("Enter time in sec: "))

# for x in range(1, countdown):
#     print(x)
#     time.sleep(1)

# for x in reversed(range(1, countdown+1)):
#     print(x)
#     time.sleep(1)

for x in range(countdown, 0, -1):
    sec = x % 60
    min = int(x / 60)
    hrs = int(x / 3600)
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("Time's up!")