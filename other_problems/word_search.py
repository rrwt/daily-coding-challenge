"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""
from typing import List


def get_neighbors(x, y, height, width, visited):
    neighbors = []

    for x2, y2 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if -1 < x2 < height and -1 < y2 < width and (x2, y2) not in visited:
            neighbors.append((x2, y2))

    return neighbors


def _search(grid, x, y, height, width, word, index, size, visited) -> bool:
    if index >= size:
        return True

    visited.add((x, y))

    for x2, y2 in get_neighbors(x, y, height, width, visited):
        if grid[x2][y2] == word[index]:
            found = _search(grid, x2, y2, height, width, word, index + 1, size, visited)
            if found:
                return True

    visited.remove((x, y))
    return False


def search(grid: List[List[str]], word: str) -> bool:
    height = len(grid)
    width = len(grid[0])
    size = len(word)

    for x in range(height):
        for y in range(width):
            if grid[x][y] == word[0] and _search(
                grid, x, y, height, width, word, 1, size, set()
            ):
                return True

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert search(board, "ABCCED") is True
    assert search(board, "SEE") is True
    assert search(board, "ABCB") is False
