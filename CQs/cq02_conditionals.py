"""the purpose of this program is act as a simple number guessing game"""

__author__: str = "730677312"


def guess_a_number() -> None:
    secret = 7
    guess = int(input("Guess a number: "))
    print("Your guess was " + str(guess))
    """defined secret and guess to use in if statement below while making input with print statement to follow"""
    if secret == guess:
        print("You got it!")
    elif secret > guess:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    """made an if statment that displays output based on guessed number"""
    return None


if __name__ == "__main__":
    guess_a_number()
