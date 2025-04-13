# Calculate the hypotenuse of triangle
import math

s1 = float(input("Enter side 1 length of triangle:  "))
s2 = float(input("Enter side 2 length of triangle:  "))

hypotenuse = math.sqrt(math.pow(s1, 2) + math.pow(s2, 2))

print("the Hypotenuse of triangle = ", round(hypotenuse, 2))