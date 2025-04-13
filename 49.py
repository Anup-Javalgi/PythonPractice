# iterables = An objext/collection that can return its element one at a time,
#             allowing it to be iterated over in a loop

l = [1, 2, 3, 4, 5]

for number in l:
    print(number)

for number in reversed(l):
    print(number)

s = {'apple', 'banana', 'coconut', 'orange'}

for fruit in s:
    print(fruit)

stri = 'bro code'

for char in stri:
    print(char)
for char in reversed(stri):
    print(char)

dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

for key, valu in dic.items():
    print(key, ':', valu)