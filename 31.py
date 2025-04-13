# shopping cart program in python

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter Price of {food} : ₹"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for f in foods:
    for p in prices:
        print(f"{f} : {p}₹")
        total = total + p
        prices.remove(p)
        break

print(f"Total : {total}₹")