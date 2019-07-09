"""
The knight is placed on the first block of an empty board and,
moving according to the rules of chess, must visit each square exactly once. 
"""


def is_valid_move(x: int, y: int, block_size: int, traversed: list):
    return 0 <= x < block_size and 0 <= y < block_size and traversed[x][y] == -1


def print_tour(traversed: list, block_size: int) -> None:
    for i in range(block_size):
        print(*traversed[i], sep=", ")


def knight_tour(
    x: int,
    y: int,
    num_moves: int,
    traversed: list,
    x_moves: list,
    y_moves: list,
    block_size: int,
):
    """
    Valid moves: (0, 0) to (64, 64)
    At any point a knight can move to a maximum of 8 different places
    """
    if num_moves == block_size * block_size:
        print_tour(traversed, block_size)
        return True

    for k in range(block_size):
        next_x = x + x_moves[k]
        next_y = y + y_moves[k]

        if is_valid_move(next_x, next_y, block_size, traversed):
            traversed[next_x][next_y] = num_moves
            if knight_tour(
                next_x, next_y, num_moves + 1, traversed, x_moves, y_moves, block_size
            ):
                return True
            traversed[next_x][next_y] = -1  # otherwise backtrack


def solve_knight_tour(block_size: int) -> None:
    assert block_size > 0

    traversed = []
    for i in range(block_size):
        traversed.append([-1] * block_size)

    # list of legal x and y moves for a knight
    x_moves = [2, 2, 1, 1, -1, -1, -2, -2]
    y_moves = [1, -1, 2, -2, 2, -2, 1, -1]

    traversed[0][0] = 0  # starting position

    if not knight_tour(0, 0, 1, traversed, x_moves, y_moves, block_size):
        print("Not possible to start from (0,0)")


if __name__ == "__main__":
    solve_knight_tour(8)
