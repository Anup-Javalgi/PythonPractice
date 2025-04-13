# Concession stand program

menu = { 'pizza'   : 3.00,
        'nachos'   : 4.50,
        'popcorn'  : 6.00,
        'fries'    : 2.50,
        'chips'    : 1.00,
        'pretzel'  : 3.50,
        'soda'     : 3.00,
        'lemonade' : 4.25 }

cart = []
total = 0

print("--------MENU--------")

for key, value in menu.items():
    print(f"{key:10} : {value:.2f}")

print("--------------------")

while True:
    food = input('Enter the selected item (q to quit) :').lower()
    if(food == 'q'):
        break
    elif menu.get(food) is not None:
        cart.append(food)

print(cart)
for c in cart:
    total = total + menu.get(c)

print(f"Total : {total:.2f}₹")