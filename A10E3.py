"""
Module Docstring

Author: Nick Stuckless

Description: Plays a guessing game with the user

Usage: A10E3.py

Parameters: None
"""

import random
#Main function plays the game 
def main():
    at_play = True
    
    while at_play:
        magic_number = random.randint(1,100)
        print("Welcome to the game")
        player_guess = get_player_guess()
        while player_guess != magic_number:
            check_player_guess(player_guess, magic_number)
            player_guess = get_player_guess()
        print("You did it! Well done.")
        at_play = replay()
        break

  
#gets player guesses      
def get_player_guess(): 
    while True:
        try: 
            guess = int(input("Guess a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else: print("Please enter a valid number")
        except ValueError: 
            print("Please enter a valid number")
#checks player guesses
def check_player_guess(real_guess, magic_number):
    if real_guess > magic_number:
        print("Too high, keep trying!")
    elif real_guess < magic_number:
        print("Too low, keep trying!")
    else: print("Invalid option")
#replay option for the players
def replay():
    while True:
        player_replay = input("Would you like to play again? (y/n): ")
        if player_replay.lower() == "y":
            return True
        elif player_replay.lower() == "n":
            return False
        else: print("Invalid option, please print 'y' or 'n'.")

if __name__ == "__main__":
    main()