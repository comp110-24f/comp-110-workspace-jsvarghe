"""Mutating functions."""

__author__: str = "730677312"


def manual_append(a: list[int], number: int) -> None:
    a.append(number)


def double(a: list[int]) -> None:
    i = 0
    while i < len(a):
        a[i] = a[i] * 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(a=list_2)
print(list_1)
print(list_2)
