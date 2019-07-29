"""
Given a 2D matrix of characters and a target word, write a function that returns
whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix: This will run the following commands:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column.
Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""
from typing import Optional


def recursive_search(
    arr: list,
    x: int,
    x_max: int,
    y: int,
    y_max: int,
    word: str,
    index: int,
    wlen: int,
    dir: str,
) -> bool:
    """
    dir: None - both directions are available
         h - horizontally
         v - vertically
    """
    if index == wlen:
        return True
    if x > x_max or y > y_max:
        return False

    if dir == "h":
        return arr[x][y] == word[index] and recursive_search(
            arr, x + 1, x_max, y, y_max, word, index + 1, wlen, "h"
        )
    else:
        return arr[x][y] == word[index] and recursive_search(
            arr, x, x_max, y + 1, y_max, word, index + 1, wlen, "v"
        )
    return False


def find_word(arr: list, word: str) -> bool:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(n)  # stack
    """
    x_max, y_max, wlen = len(arr) - 1, len(arr[0]) - 1, len(word)
    res: bool = False

    for i in range(0, x_max + 1):
        for j in range(0, y_max + 1):
            if arr[i][j] == word[0]:
                res = recursive_search(
                    arr, i + 1, x_max, j, y_max, word, 1, wlen, "h"
                ) or recursive_search(arr, i, x_max, j + 1, y_max, word, 1, wlen, "v")

            if res:
                return res

    return res


if __name__ == "__main__":
    arr: list = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]
    assert find_word(arr, "FOAM") == True
    assert find_word(arr, "MASS") == True
    assert find_word(arr, "NO") == True
    assert find_word(arr, "NAS") == False
