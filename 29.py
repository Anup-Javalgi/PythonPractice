# ------> SET : unordered and mutable, Add/Remove OK. No Duplicates

fruit = {'apple', 'grapes', 'banana', 'coconut', 'guava'}
print(fruit)

# print(dir(set))

# print(help(set))

print(len(fruit))

print('pineapple' in fruit)

# print(fruit[0])  #indexing cannot be done in set becoz they are unordered.

fruit.add('pineapple')
# fruit.add('apple') # not through any error but apple will not be added becoz set doesnt allow duplicates
print(fruit)

fruit.remove('pineapple')
print(fruit)

print(fruit.pop()) # removes + returns set item
print(fruit)

fruit.clear()
print(fruit)


# my_fset = frozenset({1, 2, 3})

# my_fset.add(4)  # ❌ This will raise an AttributeError
# my_fset.remove(2)  # ❌ This will also raise an AttributeError

# print(my_fset)  # Output: frozenset({1, 2, 3})
