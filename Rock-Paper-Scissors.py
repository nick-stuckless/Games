"""
Module Docstring

Author: Nick Stuckless

Description: Simulates a game of rock paper scissors for the user. 

Usage: python A8E2.py

Parameters: None

"""


import random


# Global variables defined, random imported #
def main():
    player_choice = get_player_choice()
    game = get_computer_choice()
    result = game_result(player_choice, game)
    print_results(result)

#Player choice function#
def get_player_choice():

    ROCK = "R"
    PAPER = "P"
    SCISSORS = "S"

    player_input = input(f"Please select Rock ({ROCK}), Paper ({PAPER}) or Scissors ({SCISSORS}):")
    if player_input == ROCK:
        print("You chose ROCK.", end='\n')
    elif player_input == PAPER:
        print("You chose PAPER.", end='\n')
    elif player_input == SCISSORS:
        print("You chose SCISSORS.", end='\n')
    else: print("You chose an invalid option") 
    return player_input.upper()
#Computer choice function#
def get_computer_choice():

    ROCK = "R"
    PAPER = "P"
    SCISSORS = "S"
    shoot = random.choice([ROCK, PAPER, SCISSORS])
    if shoot == ROCK:
        print("The computer chose ROCK.", end='\n')
    elif shoot == PAPER:
        print("The computer chose PAPER.", end='\n')
    elif shoot == SCISSORS:
        print("The computer chose SCISSORS.", end='\n')
    return shoot.upper()
#Game result function#
def game_result(get_player_choice, get_computer_choice):

    win = 1
    draw = 0
    loss = -1
    ROCK = "R"
    PAPER = "P"
    SCISSORS = "S"

    if get_player_choice == ROCK and get_computer_choice == ROCK or get_player_choice == PAPER and get_computer_choice == PAPER or get_player_choice == SCISSORS and get_computer_choice == SCISSORS:
        return draw
    elif get_player_choice == ROCK and get_computer_choice == SCISSORS or get_player_choice == SCISSORS and get_computer_choice == PAPER or get_player_choice == PAPER and get_computer_choice == ROCK:
        return win
    elif get_player_choice == ROCK and get_computer_choice == PAPER or get_player_choice == SCISSORS and get_computer_choice == ROCK or get_player_choice == PAPER and get_computer_choice == SCISSORS:
        return loss
#Print results#
def print_results(result):
    if result == 1:
        print("You Win!")
    elif result == -1:
        print("You Lose!")
    elif result == 0:
        print("Its a draw")


if __name__=="__main__":
    main()
