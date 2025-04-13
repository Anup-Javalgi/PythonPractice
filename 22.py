# format specifiers

price1 = 3000.14159 
price2 = -98700.65
price3 =12000.34

print("No of numbers after decimal")
print(f"Price 1 = {price1:.2f}")
print(f"Price 2 = {price2:.2f}")
print(f"Price 3 = {price3:.2f} \n")

print("spaces before printing prices")
print(f"Price 1 = {price1:10}")
print(f"Price 2 = {price2:10}")
print(f"Price 3 = {price3:10} \n")

print("zeros before printing prices")
print(f"Price 1 = {price1:010}")
print(f"Price 2 = {price2:010}")
print(f"Price 3 = {price3:010} \n")

print("Left justify")
print(f"Price 1 = {price1:<10}")
print(f"Price 2 = {price2:<10}")
print(f"Price 3 = {price3:<10} \n")

print("Right justify")
print(f"Price 1 = {price1:>10}")
print(f"Price 2 = {price2:>10}")
print(f"Price 3 = {price3:>10} \n")

print("Center align")
print(f"Price 1 = {price1:^10}")
print(f"Price 2 = {price2:^10}")
print(f"Price 3 = {price3:^10} \n")

print("Display positive values")
print(f"Price 1 = {price1:+}")
print(f"Price 2 = {price2:+}")
print(f"Price 3 = {price3:+} \n")

print("Space")
print(f"Price 1 = {price1: }")
print(f"Price 2 = {price2: }")
print(f"Price 3 = {price3: } \n")

print("Using delimeter")
print(f"Price 1 = {price1:,}")
print(f"Price 2 = {price2:,}")
print(f"Price 3 = {price3:,} \n")

print("Mixing format specifier")
print(f"Price 1 = {price1:+,.2f}")
print(f"Price 2 = {price2:+,.2f}")
print(f"Price 3 = {price3:+,.2f} \n")