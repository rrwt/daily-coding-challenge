"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:
    [['A','B','C','E'],
     ['S','F','C','S'],
     ['A','D','E','E']]

exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
"""
from typing import List


def verify_word_at_pos(
    board: List[List[str]],
    h: int,
    height: int,
    w: int,
    width: int,
    word: str,
    index: int,
    word_len: int,
    marked: set,
) -> bool:
    """
    Time Complexity: O(4^word_len))
    Space Complexity: O(word_len)
    """
    if index == word_len:
        return True

    for (i, j) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        y = h + i
        x = w + j

        if (
            -1 < y < height
            and -1 < x < width
            and (y, x) not in marked
            and board[y][x] == word[index]
        ):
            marked.add((y, x))

            if verify_word_at_pos(
                board, y, height, x, width, word, index + 1, word_len, marked
            ):
                return True
            else:
                marked.remove((y, x))

    return False


def exists(board: List[List[str]], word: str) -> bool:
    """
    Time Complexity: O(h * w * 4^word_len)
    Space Complexity: O(word_len)
    """
    height = len(board)
    width = len(board[0])
    word_len = len(word)

    for h in range(height):
        for w in range(width):
            if board[h][w] == word[0] and verify_word_at_pos(
                board, h, height, w, width, word, 1, word_len, {(h, w)}
            ):
                return True

    return False


if __name__ == "__main__":
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exists(b, "ABCCED") is True
    assert exists(b, "SEE") is True
    assert exists(b, "ABCB") is False
