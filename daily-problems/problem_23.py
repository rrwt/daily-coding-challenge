"""
You are given an M by N matrix consisting of booleans that represents a board.
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of
steps required to reach the end coordinate from the start. If there is no possible path,
then return null. You can move up, left, down, and right. You cannot move through walls.
You cannot wrap around the edges of the board.
For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]

and start = (3, 0) (bottom left) and end = (0, 0) (top left),
the minimum number of steps required to reach the end is 7,
since we would need to go through (1, 2) because there is a
wall everywhere else on the second row.
"""
import sys
from typing import List

step_x = 1, -1, 0, 0
step_y = 0, 0, 1, -1


def is_legal(
    board: List[List[bool]], board_rows: int, board_cols: int, new_x: int, new_y: int
) -> bool:
    if (
        -1 < new_x < board_rows
        and -1 < new_y < board_cols
        and board[new_x][new_y] is False
    ):
        return True

    return False


def shortest_path(
    board: List[List[bool]],
    board_rows: int,
    board_cols: int,
    start_x: int,
    start_y: int,
    end_x: int,
    end_y: int,
    steps: int,
) -> int:
    """
    Using backtracking. Check all the possible next steps (Depth first search)
    """
    if start_x == end_x and start_y == end_y:
        return steps

    min_steps: int = sys.maxsize

    for x, y in zip(step_x, step_y):
        new_x = start_x + x
        new_y = start_y + y

        if is_legal(board, board_rows, board_cols, new_x, new_y):
            board[new_x][new_y] = True
            min_steps = min(
                shortest_path(
                    board, board_rows, board_cols, new_x, new_y, end_x, end_y, steps + 1
                ),
                min_steps,
            )
            board[new_x][new_y] = False

    return min_steps


if __name__ == "__main__":
    board: List[List[bool]] = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False],
    ]

    board[3][0] = True

    print(shortest_path(board, len(board), len(board[0]), 3, 0, 0, 0, 0))

