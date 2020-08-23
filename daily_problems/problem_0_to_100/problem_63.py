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
    w_len: int,
    direction: str,
) -> bool:
    """
    dir: None - both directions are available
         h - horizontally
         v - vertically
    """
    if index == w_len:
        return True
    if x > x_max or y > y_max:
        return False

    if direction == "h":
        return arr[x][y] == word[index] and recursive_search(
            arr, x + 1, x_max, y, y_max, word, index + 1, w_len, "h"
        )
    else:
        return arr[x][y] == word[index] and recursive_search(
            arr, x, x_max, y + 1, y_max, word, index + 1, w_len, "v"
        )


def find_word(arr: list, word: str) -> bool:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(n)  # stack
    """
    x_max, y_max, w_len = len(arr) - 1, len(arr[0]) - 1, len(word)
    res: bool = False

    # choose starting position
    for i in range(0, x_max + 1):
        for j in range(0, y_max + 1):
            if arr[i][j] == word[0]:
                res = recursive_search(
                    arr, i + 1, x_max, j, y_max, word, 1, w_len, "h"
                ) or recursive_search(arr, i, x_max, j + 1, y_max, word, 1, w_len, "v")

            if res:
                return res

    return res


if __name__ == "__main__":
    arr_words: list = [
        ["F", "A", "C", "I"],
        ["O", "B", "Q", "P"],
        ["A", "N", "O", "B"],
        ["M", "A", "S", "S"],
    ]
    assert find_word(arr_words, "FOAM") is True
    assert find_word(arr_words, "MASS") is True
    assert find_word(arr_words, "NO") is True
    assert find_word(arr_words, "NAS") is False
