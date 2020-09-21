"""
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom
right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:
t     a     g
 h   s z   a
  i i   i z
   s     g
"""
from typing import Tuple


def set_row_and_direction(row, k, direction) -> Tuple[int, int]:
    if row == 0:
        direction = 1
    elif row == k - 1:
        direction = -1

    return min(max(row + direction, 0), k - 1), direction


def print_zig_zag(text: str, k: int) -> None:
    size = len(text)
    output = [[" "] * size for _ in range(k)]
    row = 0
    direction = 1

    for index in range(size):
        output[row][index] = text[index]
        row, direction = set_row_and_direction(row, k, direction)

    for index in range(k):
        print("".join(output[index]))

    print("-" * size)


if __name__ == "__main__":
    print_zig_zag("thisisazigzag", 1)
    print_zig_zag("thisisazigzag", 2)
    print_zig_zag("thisisazigzag", 3)
    print_zig_zag("thisisazigzag", 4)
    print_zig_zag("thisisazigzag", 5)
