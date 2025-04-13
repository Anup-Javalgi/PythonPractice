# Python compound interest calculator

principle = 0
time = 0

while (principle <= 0):
    principle = float(input("Enter the principle amount: "))

rate = float(input("Enter the rate of interest: "))
while (rate < 0):
    rate = float(input("Enter the rate of interest: "))

while (time <= 0):
    time = float(input("Enter the time in years: "))

print(f"\nYour princile amount = {principle}")
print(f"Your rate of interest = {rate}")
print(f"Your time in years = {time}")

total = principle * (1 + (rate / 100)) * time

print(f"\nBalance after {time} years = {total}₹")