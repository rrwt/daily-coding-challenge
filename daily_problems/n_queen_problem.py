"""
You have an N by N board. Write a function that returns the number of possible
arrangements of the board where N queens can be placed on the board without
threatening each other, i.e. no two queens share the same row, column, or diagonal.
"""


def is_legal_move(x: int, y: int, dim: int, board: list) -> bool:
    """
    since we know that previous rows are all occupied,
    we can reduce the number of checks
    """
    for i in range(x):  # check previous rows with current column
        if board[i][y]:
            return False

    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):  # check left upper
        if board[i][j]:
            return False

    for i, j in zip(range(x, -1, -1), range(y, dim)):  # check right upper
        if board[i][j]:
            return False

    return True


def n_queen(dim: int):
    """
    To reduce the problem size, we always place a queen in the next row.
    Afterwards we decide which column to place it in.
    In case we know that dim is even, we can reduce the time by half because
    the solution will be symmetric with respect to the x axis. 
    """

    def solution(q_placed: int):
        nonlocal ways, board
        if q_placed == dim:
            ways += 1
        else:
            for i in range(dim):
                # q_placed serves as row number too
                if is_legal_move(q_placed, i, dim, board):
                    board[q_placed][i] = 1
                    solution(q_placed + 1)
                    board[q_placed][i] = None  # backtrack

    ways: int = 0
    board: list = [[None] * dim for _ in range(dim)]
    solution(0)
    return ways


if __name__ == "__main__":
    for i in range(1, 10):
        print(i, ":", n_queen(i))
