# 2d list in python

fruits = ['apple'  , 'banana' , 'grapes'  , 'chickoo' , 'pineapple', 'guava']
vegis =  ['celery' , 'carrots', 'potatoes', 'cucumber']
meats =  ['chicken', 'fish'   , 'mutton']

groceries = [fruits, vegis, meats]

print(groceries)

print(groceries[0])

print(groceries[0][1])

print(groceries[1][2])

print("<------ Print Using Nested Loops ------>")
for item in groceries:
    for i in item:
        print(i, end=" ")
    print()

# we can also create a 2d tuple
groceries = ( ('apple'  , 'banana' , 'grapes'  , 'chickoo' , 'pineapple', 'guava'),
              ('celery' , 'carrots', 'potatoes', 'cucumber'),
              ('chicken', 'fish'   , 'mutton') )

# we cannot create a tuple made up of sets