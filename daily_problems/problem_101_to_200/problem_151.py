"""
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
replace the color of the given pixel and all adjacent same colored pixels with C.

For example,
    given the following matrix, and location pixel of (2, 2), and 'G' for green:
    B B W                   B B G
    W W W      Becomes      G G G
    W W W                   G G G
    B B B                   B B B
"""
from typing import List, Tuple


def get_neighbors(x: int, y: int, height: int, width: int) -> List[Tuple[int, int]]:
    neighbors = []

    for (nx, ny) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if -1 < nx < width and -1 < ny < height:
            neighbors.append((nx, ny))

    return neighbors


def _replace_colors(
    matrix: List[List[str]],
    start_x: int,
    start_y: int,
    height: int,
    width: int,
    color: str,
    new_color: str,
) -> List[List[str]]:

    for (x, y) in get_neighbors(start_x, start_y, height, width):
        if matrix[y][x] == color:
            matrix[y][x] = new_color
            matrix = _replace_colors(matrix, x, y, height, width, color, new_color)

    return matrix


def replace_colors(
    matrix: List[List[str]], x: int, y: int, color: str
) -> List[List[str]]:
    start_color = matrix[x][y]

    if start_color == color:
        return matrix

    matrix[x][y] = color
    return _replace_colors(
        matrix, x, y, len(matrix), len(matrix[0]), start_color, color
    )


if __name__ == "__main__":
    print(
        replace_colors(
            [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]],
            2,
            2,
            "G",
        )
    )
