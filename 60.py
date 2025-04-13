# Hangman game in Python

import random

words = ('apple', 'orange', 'banana', 'coconut', 'pineapple')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')
hangman_art = {0: ("+---+",
                   "|   |",
                   "    |",
                   "    |",
                   "    |",
                   "    |",
                 "========="),
               1: ("+---+",
                   "|   |",
                   "O   |",
                   "    |",
                   "    |",
                   "    |",
                 "========="),
                2: ("+---+",
                   "|   |",
                   "O   |",
                   "|   |",
                   "    |",
                   "    |",
                 "========="),
                3: ("+---+",
                   "|   |",
                   "O   |",
                  "/|   |",
                   "    |",
                   "    |",
                 "========="),
                4: ("+---+",
                   "|   |",
                   "O   |",
                  "/|\  |",
                   "    |",
                   "    |",
                 "========="),
                5: ("+---+",
                   "|   |",
                   "O   |",
                  "/|\  |",
                  "/    |",
                   "    |",
                 "========="),
                6: ("+---+",
                   "|   |",
                   "O   |",
                  "/|\  |",
                  "/ \  |",
                   "    |",
                 "========="),}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ['_'] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Invalid Input!")
            continue

        elif guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong_guesses==len(hangman_art):
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Lose!")
            is_running = False

if __name__ == '__main__':
    main()

