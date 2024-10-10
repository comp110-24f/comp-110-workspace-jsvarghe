"""import assignment"""

__author__ = "730677312"


def get_coords(xs: str, ys: str) -> None:
    index = 0
    while index < len(xs):
        index2 = 0
        while index2 < len(ys):
            print("(" + str(xs[index]) + "," + str(ys[index2]) + ")")
            index2 += 1
        index += 1
