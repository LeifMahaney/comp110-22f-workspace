"""EX02 - One shot Wordle."""

__author__ = "730468655"  
"""This is normally an email but in class we use PID because it is easier to establish who did what"""

secret_word: str = "python"
character: int = len(secret_word)
guess: str = input(f"What is your {character}-letter guess?: ")   
"""This will prompt the user to type an input"""
WHITE_BOX: str = "\U00002B1C"  
"""LInes 7-9 are coded emojis, that print either a green, yellow, or white box"""
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" 
while len(guess) != len(secret_word):
    guess = input(f"That was not {character} letters! Try again: ")  
    """if the user originally does not type an answer equivilant in length to the secret word than they will be prompted to enter a new input"""
index: int = 0  
"""Is a new variable being introduced"""
emoji: str = ""  """New string value"""
while index < len(secret_word):  
    """This means that while index is less than the length of the secret word than itll go onto the if else statement and everything indented underneath it (everything underneath the while statement will repeat until completed)"""
    if guess[index] == secret_word[index]:  
        """This saying that if the guess first variable is the same as the secret word a green box will print"""
        emoji = emoji + GREEN_BOX  
        """Green box will print and the value of emoji will be altered"""
    else:  
        """This occurs when the if statement is false."""
        train: bool = False  
        """New variable being established"""
        snakes: int = 0  
        """New varible being established"""
        while not train and snakes < len(secret_word):  
            """This is saying while the boolen varible is not true and the index is less than the length of the secret word than the indented lines below will run"""
            if guess[index] == secret_word[snakes]:  
                """This line is the same however the varible index is adjusted for the new variable snakes that was recently established"""
                train = True  
                """If this if statement is right than train will become True """
            else:
                snakes = snakes + 1  
                """If the statement results as false, the value of snakes will increase by one"""
        if train:  
            """If train equal True"""
            emoji = emoji + YELLOW_BOX  
            """When Train equals true a yellow box will print"""
        else:
            emoji = emoji + WHITE_BOX  
            """When this statement is true a white box will print"""
    index = index + 1
print(emoji)  
"""Will print the variable emoji after it has been ran through the program above"""
if guess == secret_word:  
    """If the guess is the secret word this line will run"""
    print("Woo! You got it!")  
    """When the guess is right this line will print"""
else:
    print("Not quite. Play again soon!")  
    """If the guess is wrong this line will print"""