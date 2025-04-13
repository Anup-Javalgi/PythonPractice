import random

# print(dir(random))
# print(help(random))

low = 1
high = 100
options = ('rock', 'paper', 'sissors')
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# number = random.randint(low, high)

# number = random.random() # return floating point number between 0 and 1

option = random.choice(options)

# print(number)
print(option)

random.shuffle(cards)
print(cards)