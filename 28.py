# collection = single variable used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster than list

fruit = "apple"
print(fruit)

# ---> LISTS : ordered and changeable. Duplicates OK
fruit = ['apple', 'grapes', 'banana', 'coconut', 'guava']
print(fruit)
print(fruit[0])
print(fruit[2])

for f in fruit:
    print(f)

# print(dir(fruit))

# print(help(list))

print(len(fruit))

print("apple" in fruit)

fruit.append('pineapple')
print(fruit)

fruit.remove('pineapple')
print(fruit)

fruit.insert(0, 'pineapple')
print(fruit)

fruit.sort()
print(fruit)

fruit.reverse()
print(fruit)

print(fruit.index('apple'))

print(fruit.count('banana'))

fruit.clear()
print(fruit)