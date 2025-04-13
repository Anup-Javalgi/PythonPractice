# Shopping cart program

item = input("What item u want to purchace: ")
price = float(input("What is its price: "))
quantity = int(input("How many whould u like: "))
total = quantity*price

print("// YOUR BILL //")
print(f"Item : {item}")
print(f"Price : {price}")
print(f"Quantity : {quantity}")
print(f"Total: {total}₹ including all taxes")