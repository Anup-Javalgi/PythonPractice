#  Dictionary in Python : A collection of {Key:value} pairs
#                          ordered and changeable. No Duplicates

capitals = { 'USA'   : 'Washington D.C.',
            'India'  : 'New Delhi',
            'China'  : 'Beijing',
            'Russia' : 'Moscow' }

# print(dir(dict))
# print(help(dict))

print(capitals.get('USA'))
# print(capitals.get('xyz')) # returns none becoz key not in the dict
ayz = None

if capitals.get("China"):
    print(capitals.get("China"))
    print("That capital exists")
else:
    print("That capital doesnt exists")

capitals.update({'Germany' : 'Berlin'})
# capitals.update({'USA':'Detroit'})

capitals.pop("India")
print(capitals)

capitals.popitem()
print(capitals)

print("Printing keys")
keys = capitals.keys()
print(keys)  # keys are object which ressembles a list
for key in keys:
    print(key)

print("Printing values")
values = capitals.values()
print(values)
for val in values:
    print(val)

print("Printing items")
items = capitals.items()
print(items)  # dict object which ressembles a 2d list of tuples
for key, val in items:
    print(key, val)

capitals.clear()
print(capitals)