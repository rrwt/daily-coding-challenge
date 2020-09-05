"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
"""
from typing import List, Tuple


def get_neighbors(
    x: int, y: int, height: int, width: int, visited: set
) -> List[Tuple[int, int]]:
    neighbors = []

    for x2, y2 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if -1 < x2 < height and -1 < y2 < width and (x2, y2) not in visited:
            neighbors.append((x2, y2))

    return neighbors


def visit_neighbors(
    matrix: List[List[str]], x: int, y: int, height: int, width: int, visited: set
) -> set:
    for x2, y2 in get_neighbors(x, y, height, width, visited):
        if matrix[x2][y2] == "1" and (x2, y2) not in visited:
            visited.add((x2, y2))
            visited = visit_neighbors(matrix, x2, y2, height, width, visited)

    return visited


def num_islands(matrix: List[List[str]]) -> int:
    if not matrix:
        return 0

    visited = set()
    height = len(matrix)
    width = len(matrix[0])
    count = 0

    for i in range(height):
        for j in range(width):
            if matrix[i][j] == "1" and (i, j) not in visited:
                visited.add((i, j))
                count += 1
                visited = visit_neighbors(matrix, i, j, height, width, visited)

    return count


if __name__ == "__main__":
    assert (
        num_islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )

    assert (
        num_islands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
