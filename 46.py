# Arbitary argument : means varring argument
                    # we dont know how many arguments user will pass
# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
# * unpacking operator


#---------> *args

def add(*args):
    total = 0
    # print(type(args))  # packs all argument in a tuple
    for arg in args:
        total += arg
    return total
print(add(1, 2, 3))

# we can also cange name eg: *nums

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name('Hello', 'Mr.', 'Anup', 'Javalgi')