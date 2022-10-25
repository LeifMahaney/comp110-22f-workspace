"""A Guessing Game!"""

__author__ = "730468655"

import random

points: int = 0
player: str = ""
GREEN_BOX: str = "\U0001F7E9"


def greet() -> None:
    """This is the greet function that stores the players name and greets them."""
    global player
    print("Welcome, there are three options Coinflip, Number Guessing, or Exit (to leave the game)")
    player = input("Please enter your name ")
    
    
def coinflip(initial_guess: int) -> None:
    """This function creates a game in which the user guesses head or tails."""
    global points
    correct: int = random.randint(1, 2)
    while initial_guess == correct:
        correct = random.randint(1, 2)
        points += 1
        if points == 1:
            print(f"Correct. You now have {points} point! ")
        elif points != 1:
            print(f"Correct. You now have {points} points! ")
        initial_guess = int(input("Guess again: "))
    if initial_guess != correct:
        print(f"Sorry that was incorrect, thank you for playing! You accumulated {points} points.")
        

def number_guessing(initial_guess1: int) -> int:
    """This function creates a game that generates a random number between 1-5 and the player must guess the number."""
    index: int = 1
    emoji: str = ""
    random_num: int = random.randint(1, 5)
    while initial_guess1 != random_num:
        initial_guess1 = int(input("Incorrect, please enter a new guess or type 6 to exit. "))
        index += 1
    if initial_guess1 == 6:
        print(f"You finished with {points} points. ")
        quit()
    emoji += GREEN_BOX
    print(emoji)
    print(f"Congrats you guessed the correct integer, it took you {index} tries ") 
    return 5


def procedure() -> None:
    """This function stores all the procedures and allows the game to continuosly run."""
    global points
    print("Which game would you like to play: Coinflip, Number Guessing, or Exit (to leave the game)")
    game: str = input("Type C for Coinflip. Type N for Number Guessing, and E to Exit ")
    while game == "C" or game == "N":
        if game == "C":
            print("Coinflip is a gussing game in which you will guess heads or tails. If you are correct you will continue guess. ")
            initial_guess: int = int(input("Type 1 for heads and 2 for tails. "))
            coinflip(initial_guess)
            game = input("If you would like to play again type C, If you would like to play Number Guessing type N and if you would like to exit type E. ")
        elif game == "N":
            initial_guess1: int = int(input("Enter a number between 1-5. "))
            points += number_guessing(initial_guess1)
            game = input("If you would like to play again type C, If you would like to play Number Guessing type N and if you would like to exit type E. ")
        elif game == "E":
            print(f"You finished with {points} points. ")
            quit()
    if game == "E":
        print(f"You finished with {points} points. ")
        quit()
    
    
def main() -> None:
    """This is the main function and calls all of the other functions."""
    greet()     
    procedure()
        

if __name__ == "__main__":
    main()