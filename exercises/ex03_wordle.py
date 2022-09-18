"""EX03 - Structured Wordle."""
__author__ = "730468655"


def contains_char(search: str, single: str) -> bool:
    """Two variables are being declares as string values."""
    assert len(single) == 1
    index: int = 0
    while index < len(search):
        if search[index] == single:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Two new variables that represent the emoji string."""
    assert len(guess) == len(secret)
    GREEN_BOX: str = "\U0001F7E9"
    WHITE_BOX: str = "\U00002B1C"        
    YELLOW_BOX: str = "\U0001F7E8" 
    index: int = 0
    answer: str = ""
    while index < len(secret):
        if guess[index] == secret[index]: 
            answer += GREEN_BOX 
        elif contains_char(secret, guess[index]):
            answer += YELLOW_BOX
        else:
            answer += WHITE_BOX
        index += 1
    return answer


def input_guess(length: int) -> str:
    """One new variable introduced as an integer value."""
    guess: str = input(f"Enter a {length} character word: ") 
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    guess: str = ""
    round: int = 1
    while round <= 6 and guess != secret:
        print(f"=== Turn {round}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {round}/6 turns!")
        elif round == 6:
            print("X/6 - Sorry, try again tomorrow!")
        round += 1


if __name__ == "__main__":
    main()