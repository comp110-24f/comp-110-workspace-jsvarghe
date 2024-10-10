"""Summing the elements of a list using different loops"""

__author__: str = "730677312"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    total = 0
    for i in vals:
        total += i
    return total


def f_range_sum(vals: list[float]) -> float:
    total = 0

    for i in range(1, len(vals)):
        total += vals[i]

    return total
