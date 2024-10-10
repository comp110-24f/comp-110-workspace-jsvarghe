"""the purpose of thuis program is to practice using a while loop"""

__author__: str = "730677312"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1

    return count
