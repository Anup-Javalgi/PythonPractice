# list comprehension in python
# A concise way to create list in python
# compact and esier to read tha traditional loops
# [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x*2)

# print(doubles)

print("------List Comprehension------")
doubles = [x for x in range(1, 11)]
print(doubles)

doubles = [x*2 for x in range(1, 11)]
print(doubles)

doubles = [x*x for x in range(1, 11)]
print(doubles)

#-----------------------------------------------------

fruits = [fruit.upper() for fruit in ['apple', 'banana', 'coconut', 'orange' , 'grapes']]
print(fruits)

fruits = [fruit[0] for fruit in ['apple', 'banana', 'coconut', 'orange' , 'grapes']]
print(fruits)


#-----------------------------------------------------
numbers = [1, -2, 3, -4, 5, -6]
numbers = [abs(num) for num in numbers]
print(numbers)

numbers = [1, -2, 3, -4, 5, -6]
numbers = [num for num in numbers if num>=0]
print(numbers)

numbers = [1, -2, 3, -4, 5, -6]
numbers = [num for num in numbers if num<=0]
print(numbers)