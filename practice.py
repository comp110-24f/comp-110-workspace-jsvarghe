def practice(word: str) -> int:
    index = 0
    counter = 0
    while index < len(word):
        if "h" == word[index]:
            counter += 1
        index += 1
    return counter


print(practice(word="howdh"))
