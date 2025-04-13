# Logical Operators (and, or, not)

# Logical or

temp = 15
is_raining = False

if (temp>35) or (temp<0) or (is_raining):
    print("the outside event is cancelled")
else:
    print("The outdoor event is still scheduled")

# Logical and

temp = 29
is_sunny = True

if (temp>=28) and is_sunny:
    print("Its hot outside")
    print("Its sunny")
else:
    print("Its cold outside")

# Logical not

temp = 29
is_sunny = False
if (temp>=28) and not is_sunny:
    print("Its hot outside")
    print("Its sunny")
else:
    print("Its cold outside")