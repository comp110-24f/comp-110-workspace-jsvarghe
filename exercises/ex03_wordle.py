"""The purpose of this program is to mimic wordle"""

__author__: str = "730677312"


def input_guess(guess_length: int) -> str:
    """this function ensures the guess length matches the word and continues on if it does, and if it doesnt they show an error"""
    while True:
        guess = input(f"Enter a {guess_length} character word: ")
        if len(guess) == guess_length:
            return guess
        else:
            """if the length doesnt match"""
            print(f"That wasn't {guess_length} chars! Try again.")


def contains_char(searched_str: str, character_searched: str) -> bool:
    """purpose of this function is to find occurances of a certain character in the word inputed"""
    """character searched must be 1 character"""
    assert len(character_searched) == 1
    index = 0
    while index < len(searched_str):
        """if the letter is in the word at all it will return as true"""
        if searched_str[index] == character_searched:
            """if this is true then we need to connect it to the yellow emoji"""
            return True
        else:
            index += 1

    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """the purpose of this function is to compare the guess and the actual word and return emojies letting the user know how close they were"""
    assert len(user_guess) == len(secret_word)
    """the three emojis that need to be placed based on the guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    """ this variable will be used to add onto and create a string of emojis as a result of a guess"""
    emoji_result = ""
    while index < len(user_guess):
        """if the letter matches the postion of the secret word it will spit out the green emoji"""
        if user_guess[index] == secret_word[index]:
            emoji_result += GREEN_BOX
        elif contains_char(
            searched_str=secret_word, character_searched=user_guess[index]
        ):
            """if the character is in the word at all then the yellow emoji shows"""
            emoji_result += YELLOW_BOX
        else:
            """if the character is not in the word it spits out the white emoji"""
            emoji_result += WHITE_BOX
        index += 1
    return emoji_result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 1
    max_turns = 6
    won = False

    while turns <= max_turns and not won:
        """while turns is within 6 it will print out what turn it is on until they win"""
        print(f"=== Turn {turns}/{max_turns} ===")

        guess = input_guess(len(secret))
        """The result of the turn will be printed using the emjoi_result function we created earlier"""
        emoji_result = emojified(guess, secret)
        print(emoji_result)
        " if the guess is equal to the secret word the use wins and we can change won to true"
        if guess == secret:
            won = True
        else:
            turns += 1
    if won:
        """if the word matches we can print oiut a winning message"""
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        """if the guesses are wrong and the 6th turn is used then we print out a message saying they lost"""
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    """the heart of the program"""
    main(secret="codes")
