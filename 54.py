# Modules : A file containing code you want to include in your program
#           use import to include a module (built-in or your own)
#           useful to break up a large program reusable seperate files

# import math as m

# from math import pi

# print(help('math'))

#  print(help('module))

# print(m.sin(45))

# print(pi)

from math import e

a, b, c, d, e = 1, 2, 3, 4, 5

print(e)      # value of e will be 5, but not the value in the module
print(e ** a)
print(e ** b)
print(e ** c)
print(e **d)
print(e ** e)


import example1  # it user defined module

result = example1.pi
print(result)
result = example1.square(3)
print(result)
result = example1.cube(3)
print(result)
result = example1.circumference(3)
print(result)
result = example1.area(3)
print(result)
