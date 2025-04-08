
#            ''' Python Slot Machine game''' 
# Time for some gambling :>😈 

import sys
import os
import time
import random

def spin_row():
    symbols = ['🍋', '🍉', '🍒' ,'🍓', '⭐']
    return [random.choice(symbols) for _ in range(3)]
      
def print_row(row):
    symbols = ['🍋', '🍉', '🍒', '🍓', '⭐']
    print("*****************************\n")
    
    # Simulate spinning by printing all symbols and clearing them
    for _ in range(10):  # Number of spins
        spinning_row = [random.choice(symbols) for _ in range(3)]
        print(" | ".join(spinning_row), end="\r")  # Overwrite the same line
        time.sleep(0.2)  # Delay to simulate spinning

    # Print the final row
    print(" | ".join(row))
    print("\n*****************************")
    
    ## key tip in this function :-
    # Clearing Output: The end="\r" ensures that the output is overwritten on the same line, creating the effect of clearing the previous symbols.

def payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍋':
            return bet*2
        elif row[0]=='🍉':
            return bet*3
        elif row[0]=='🍒':
            return bet*4
        elif row[0]=='🍓':
            return bet*5
        elif row[0]=='⭐':
            return bet*6    
    return 0 

def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)  # Write each character to the output
        sys.stdout.flush()      # Ensure it is displayed immediately
        time.sleep(delay)       # Add a delay between characters
    print()  # Move to the next line after the text is printed


def main():
    print()
    print("****************************************\n")
    type_out("WELCOME TO PYTHON SLOTS GAME. TRY YOUR LUCK AND WIN THE GAME.")
    type_out("You will deposit money for the game start.")
    print("SYMBOLS: 🍋 🍉 🍒 🍓 ⭐")
    print("\n****************************************\n\n")

    balance = int(input("Enter the amount to deposit: "))
    
    
    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("\nEnter your betting amount:  ")

        if not bet.isdigit():
            print('\nPlease enter a valid number')
            continue
        
        bet = int(bet)

        if bet>balance:
            print('\nInsufficient Funds.')
            continue
        if bet<=0:
            print('\nBet should be greater than zero.')
            continue
        
        balance-=bet
        
        row = spin_row()
        print("\nSpinning....\n")
        
        print_row(row)

        profit = payout(row, bet)
        if profit>0:
            print(f"You won ${profit}.")
        else:
            print("\nSorry You Lost.\n")
        balance+=profit
        
        print(f"Your current Balance: {balance}.")

        again = input("\nDo you want to play again? (Y/N): ").upper()
        if again != "Y":
            type_out('Quitting....')
            break
        
    print("\n***********************************************\n")
    type_out('GAME OVER! THANKYOU FOR PLAYING.')
    print("\n***********************************************\n")
    
if __name__=='__main__':
   main()