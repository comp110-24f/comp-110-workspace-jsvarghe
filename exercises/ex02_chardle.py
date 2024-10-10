"""The purpose of this program is to mimic wordle"""

__author__: str = "730677312"


def input_word() -> str:
    """define input from user"""
    Word = input("Enter a 5-character word: ")
    if len(Word) == 5:
        """if length is 5 then it will print this"""

    else:
        """if length is not 5 then it will print this"""
        print("Error: Word must contain 5 characters.")
        """exit right after requirement was not met to prevent code from continuing"""
        exit()

    return Word


def input_letter() -> str:
    """takes user input for letter and assigns it to a variable"""
    letter = input("Enter a single character: ")
    """checks length of input to make sure it follows requirements"""
    if len(letter) == 1:
        """if length is 5 it will continue"""

    else:
        """if length is not 1 then it will print this"""
        print("Error: Character must be a single character.")
        """exits code if error meessage needs to be displayed"""
        exit()

    return letter


def contains_char(word_received: str, letter_received: str) -> None:
    """defining index and matching at 0 in order to count both accurately"""
    index = 0
    matching = 0
    """prints to user that the function is searching for the letter input in the word input"""
    print("Searching for " + letter_received + " in " + word_received)
    """this while loop runs until index is equal to the length of the word input"""
    while index < len(word_received):
        if letter_received == word_received[index]:
            print(letter_received + " found at index " + str(index))
            """increases matching variable when letter input is found in word input"""
            matching = matching + 1
        index = index + 1
    """prints whats needed when no letters are found"""
    if matching == 0:
        print("No instances of " + letter_received + " found in " + word_received)

    elif matching == 1:
        print(
            str(matching)
            + " instance of "
            + letter_received
            + " found in "
            + word_received
        )
    else:
        print(
            str(matching)
            + " instances of "
            + letter_received
            + " found in "
            + word_received
        )

    return None


"""used to put all code together """


def main() -> None:
    contains_char(word_received=input_word(), letter_received=input_letter())


if __name__ == "__main__":
    main()
