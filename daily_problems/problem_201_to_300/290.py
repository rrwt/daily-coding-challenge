"""
On a mysterious island there are creatures known as Quxes
which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing
next to each other, they can transform into a single
creature of the third color.
Given N Quxes standing in a line, determine the smallest
number of them remaining after any possible sequence of
such transformations.

For example,
    given the input ['R', 'G', 'B', 'G', 'B'],
    it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
    ----------------------------------------
    ['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
    ['B', 'B', 'G', 'B']      | (B, G) -> R
    ['B', 'R', 'B']           | (R, B) -> G
    ['B', 'G']                | (B, G) -> R
    ['R']                     |
"""
from typing import List


def transformation(colors: List[str]) -> List[str]:
    c_set = {"R", "B", "G"}

    while (size := len(colors)) > 1:
        merged = False

        for index in range(size - 1):
            if colors[index] != colors[index + 1]:
                colors[index] = c_set.difference(
                    {colors[index], colors[index + 1]}
                ).pop()
                merged = True
                del colors[index + 1]
                break

        if merged is False:
            break

    return colors


if __name__ == "__main__":
    assert transformation(["R", "G", "B", "G", "B"]) == ["R"]
