# weight converter 

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds (k or l): ")

if (unit == 'k'):
    print(f'{weight} Kgs = ', round(weight*2.20462, 2), 'Lbs')
elif(unit == 'l'):
    print(f'{weight} Lbs = ', round(weight*0.453592, 2), 'Kgs')
else:
    print("Entered unit not found.")