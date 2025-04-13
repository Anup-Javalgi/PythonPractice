# while loop

name = input("Enter your name: ")

# if name=="":
#     print("You do not enter you name")
# else:
#     print(f"Hello {name}")

while (name==""):
    print("You do not enter you name")
    name = input("Enter your name: ")

print(f"Hello {name}")

#######################################

food = input("Enter you favourite food (q to quit):")

while not(food == 'q'):
    print(f"You like {food}")
    food = input("Enter you favourite food (q to quit):")

print("Bye Bye!!!")