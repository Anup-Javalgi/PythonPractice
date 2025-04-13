# ------> TUPLE : ordered and unchangeable. Duplicates OK. Faster than list

fruit = ('apple', 'grapes', 'banana', 'coconut', 'guava')

# print(dir(tuple))

# print(help(tuple))

print(fruit.index('apple'))

print(fruit.count('banana'))

# Tuple unpacking
a, b, c, d, e = ('apple', 'grapes', 'banana', 'coconut', 'guava')
print(a, b, c, d, e) 