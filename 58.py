# Python Slot Machine

import random
import time

def spin_row():
    symbols = ['❤️', '🍉', '⭐', '🔔' ,'🍋']
    result = []
    for symbol in range(3):
        result.append(random.choice(symbols))
    return result

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '❤️':
            return bet*3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100
    print("##########################")
    print("Welcome to python slots")
    print("Symbols: ❤️ 🍉⭐🔔🍋")
    print("##########################")

    while balance > 0:
        print(f"Current balance: {balance}₹")
        bet = input("place bet amount: ₹")
        if not bet.isdigit():
            print("Invalid Bet!")
            continue
        else:
            bet = int(bet)

        if bet>balance:
            print("Insufficiant balance")
            continue
        elif bet<=0:
            print("Bet must be greater than 0")
            continue
        else:
            print(f"Bet placed : {bet}₹")
            row = spin_row()
            print("Spinning....")
            time.sleep(2)
            print_row(row)
            payout = get_payout(row, bet)
            if payout > 0:
                print(f"Congrats you Won : {payout}₹")
                balance+=payout
                print(f"Balance Left : {balance}₹")
            else:
                print("Sorry you lost this round")
                balance -= bet
                print(f"Balance Left : {balance}₹")
            
            if balance<=0:
                break
            else:
                play = input("Want to play next round?(y/n): ").lower()
                if play == 'y':
                    continue
                else:
                    break
 
    print("******************")
    print("Thanks for playing")
    print("******************")

if __name__ == '__main__':
    main()