#----------> **kwargs

def print_address(**kwargs):
    # print(type(kwargs))
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street='123 Fake St.', 
              city='Detroit', 
              state='michigan',
              zip='54321')