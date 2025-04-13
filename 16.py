# Temperature Converter

temp = float(input("Enter Temperature: "))
unit = input("Enter unit of temperature in Fahrenheit or celcius(f, c): ")

if (unit=='f'):
    print(f"{temp} °F = ", round((temp-32)*(5/9), 2), "°C")
elif (unit=='c'):
    print(f"{temp} °C = ", round((temp*(9/5))+32, 2), "°F")
else:
    print("Entered unit not found.")