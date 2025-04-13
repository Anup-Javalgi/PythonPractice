# number guessing game in python

import random

lowest_num = 1
highest_num = 100

answer  = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("------Python number GUssing Game------")
print(f"Select number between ({lowest_num}, {highest_num})")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if (guess < lowest_num) and (guess > highest_num):
            print("The number is out of range")
            print(f"Please select number between ({lowest_num}, {highest_num})")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was: {answer}")
            print(f"Number of guess: {guesses}")
            is_running = False

    else:
        print("Invalid Guess!")
        print(f"Please select number between ({lowest_num}, {highest_num})")