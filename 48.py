# using *args and **kwargs together

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")

shipping_label('Dr.', 'Spongebob', 'Squarepants', 'III',
              street='123 Fake St.', 
              city='Detroit', 
              state='michigan',
              zip='54321')

# we cant write args followed by kwargs
# but not kwargs followed by *argsbecoz positional
# arguments should be mentioned first according to syntax