"""Wordle Game Implementation."""

__author__ = "YOUR_PID_HERE"  # Replace with your 9-digit PID


def input_guess(secret_word_len: int) -> str:
    """Prompt user for a guess until the guess is of the correct length."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if the secret word contains the guessed character."""
    assert len(char_guess) == 1  # Ensure char_guess is a single character
    index = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji representation of the guess compared to the secret word."""
    result = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += "🟩"  # Green for correct position
        elif contains_char(secret, guess[i]):
            result += "🟨"  # Yellow for wrong position
        else:
            result += "⬜"  # White for not present
    return result


def main() -> None:
    """Main function to run the Wordle game."""
    secret_word = "codes"  # Set your secret word here
    max_turns = 6
    turn = 1

    while turn <= max_turns:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))

        if guess == secret_word:
            print(f"You won in {turn}/{max_turns} turns!")
            return

        turn += 1

    print("X/6 - Sorry, try again tomorrow!")


# Run the game
if __name__ == "__main__":
    main()
