"""List utility functions"""

__author__: str = "730677312"


def all(list_int: list[int], num: int) -> bool:
    if len(list_int) == 0:
        return False

    for i in list_int:
        if i == num:
            return False

    return True


def max(list_int: list) -> int:

    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")

    max = list_int[0]
    for i in range(1, len(list_int)):
        if list_int[i] > max:
            max = list_int[i]

    return max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    i = 0
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            return False
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    for i in range(len(list_2)):
        list_1.append(list_2[i])
