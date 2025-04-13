# default arguments : A default value for certain parameters
#                     defaultis used when that argument is omitted
import time

def net_price(list_price, discount=0, tax=0.05):    # default parameters
    return list_price*(1-discount)*(1+tax)

print(net_price(500))

def count(end, start=0):  # default argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done")

count(10)