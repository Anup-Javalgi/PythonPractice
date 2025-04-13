# multithreading in python
'''
Used to perform multiple task concurrently(multitasking)
good for I/O bound tasks like reading files or fetching data from APIs
threading.Thread(target=my_function)
'''

import threading
import time

# def walk_dog():
#     time.sleep(5)
#     print("You finish walking the dog")

# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")

# def get_mail():
#     time.sleep(1)
#     print("You got the mail")

# walk_dog()
# take_out_trash()
# get_mail()

# chore1 = threading.Thread(target=walk_dog)
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # .join() Waits for all chore to complete
# chore1.join()
# chore2.join()
# chore3.join()
# print("All chores are completed")



def walk_dog(first, last):
    time.sleep(5)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(1)
    print("You got the mail")

chore1 = threading.Thread(target=walk_dog, args=("scooby", "doo"))
# chore1 = threading.Thread(target=walk_dog, args=("scooby", ))
chore1.start()
 
chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()
print("All chores are completed")