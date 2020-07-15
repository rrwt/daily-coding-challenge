"""
You have an N by N board. Write a function that, given N,
returns the number of possible arrangements of the board
where N queens can be placed on the board without threatening
each other, i.e. no two queens share the same row, column, or diagonal.
"""


def is_valid(board: list, n: int, x: int, y: int) -> bool:
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 1:
        return False

    # check same column. no need to check same row.
    for i in range(x):
        if board[i][y] == 1:
            return False

    # check upper left
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return False

    # check upper right
    for i, j in zip(range(x, -1, -1), range(y, n)):
        if board[i][j] == 1:
            return False

    return True


def n_queen(board: list, n: int, next_x: int) -> int:
    """
    Set a fixed x and try to find possible y for it.
    Time complexity: O(n!)
    """
    if next_x == n:
        return 1
    else:
        count = 0
        for next_y in range(n):
            if is_valid(board, n, next_x, next_y):
                board[next_x][next_y] = 1
                count += n_queen(board, n, next_x + 1)
                board[next_x][next_y] = 0

        return count


def n_queen_count(n: int) -> int:
    if n < 1:
        return 0
    if n == 1:
        return 1

    return n_queen([[0] * n for i in range(n)], n, 0)


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, n_queen_count(i))
