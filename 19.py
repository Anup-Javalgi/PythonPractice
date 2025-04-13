# Working with Strings

name = input("Enter your full name: ")

print(len(name))

print(name.find('b'))  # finds index of first occurence.

print(name.rfind('b')) # finds index of last occurence. 

print(name.capitalize())

print(name.upper())

print(name.lower())

print(name.isdigit())  # checks wheather the string is digital or not

print(name.isalpha())  # checks wheather the string is alphabetical or not

print(name.count('b'))

print(name.replace('b', 'a'))

# print(help(str))