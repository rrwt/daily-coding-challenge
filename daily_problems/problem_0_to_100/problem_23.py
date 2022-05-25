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
from collections import deque
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
    Sub optimal solution.
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


def is_legal_bfs(x, y, len_x, len_y, matrix, distance_bfs):
    return (
        -1 < x < len_x
        and -1 < y < len_y
        and matrix[x][y] is False
        and distance_bfs[x][y] == sys.maxsize
    )


def shortest_path_bfs(matrix, len_x, len_y, start_x, start_y, end_x, end_y) -> int:
    """
    Using BFS. BFS generates the shortest path from point 1 to point 2 in a matrix/graph.
    Optimal Solution.
    Time Complexity: O(len_x * len_y)
    Space Complexity: O(len_x * len_y)
    """

    distance_bfs = [[sys.maxsize] * len_x for _ in range(len_y)]
    distance_bfs[start_x][start_y] = 0
    neighbors = deque([(start_x, start_y, 1)])
    visited = set()

    while neighbors:
        cur_x, cur_y, distance = neighbors.popleft()
        visited.add((cur_x, cur_y))

        for x, y in zip(step_x, step_y):
            new_x = cur_x + x
            new_y = cur_y + y

            if (new_x, new_y) in visited:
                continue

            if is_legal_bfs(new_x, new_y, len_x, len_y, matrix, distance_bfs):
                distance_bfs[new_x][new_y] = distance

                if new_x == end_x and new_y == end_y:
                    return distance

                neighbors.append((new_x, new_y, distance + 1))

    return sys.maxsize


if __name__ == "__main__":
    board: List[List[bool]] = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False],
    ]

    board[3][0] = True

    print(shortest_path(board, len(board), len(board[0]), 3, 0, 0, 0, 0))
    print(shortest_path_bfs(board, len(board), len(board[0]), 3, 0, 0, 0))
