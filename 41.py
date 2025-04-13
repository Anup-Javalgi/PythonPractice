# Rock Papper Sissors Game In Python

import random

options = ('rock', 'paper', 'sissors')
playing = True

while playing:
    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input("Enter your choice ('rock', 'paper', 'sissors'): ").lower()

    print(f"Player Choice : {player_choice}")
    print(f"Computer Choice : {computer_choice}")

    if player_choice == computer_choice:
        print("Its Tie!")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("Player Wins!")
    elif player_choice == 'sissors' and computer_choice == 'paper':
        print("Player Wins!")
    elif player_choice == 'rock' and computer_choice == 'sissors':
        print("Player Wins!")
    else:
        print("Computer Wins!")

    if not input("Play again? y/n: ").lower() == 'y':
       playing = False

print("Thanks for playing!")