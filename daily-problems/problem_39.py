"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply:
    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
Implement Conway's Game of Life. It should be able to be initialized with a starting
list of live cell coordinates and the number of steps it should run for.
Once initialized, it should print out the board state at each step.
Since it's an infinite board, print out only the relevant coordinates,
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

X_MIN, X_MAX, Y_MIN, Y_MAX = 100, 0, 100, 0


def update_range(board: list, board_size: int, first: bool = False) -> None:
    """
    Helpful in reducing checks and if we don't want to print the entire board.
    An existing life cannot modify any life that is not it's immediate neighbour
    """
    global X_MIN, X_MAX, Y_MIN, Y_MAX
    if first is True:
        for i in range(board_size):
            for j in range(board_size):
                if board[i][j] == "*":
                    X_MIN = min(i, X_MIN)
                    X_MAX = max(i, X_MAX)
                    Y_MIN = min(j, Y_MIN)
                    Y_MAX = max(j, Y_MAX)

        X_MIN = max(X_MIN - 1, 0)
        X_MAX = min(X_MAX + 1, board_size - 1)
        Y_MIN = max(Y_MIN - 1, 0)
        Y_MAX = min(Y_MAX + 1, board_size - 1)
    else:
        if X_MIN > 0:  # get new x_min
            found: bool = False

            for j in range(Y_MIN, Y_MAX + 1):
                if j < board_size:
                    if board[X_MIN][j] == "*":
                        X_MIN -= 1
                        break
                    elif board[X_MIN + 1][j] == "*":
                        found = True
            else:
                if not found:
                    X_MIN += 1

        if X_MAX < board_size - 1:  # get new x_max
            found: bool = False

            for j in range(Y_MIN, Y_MAX + 1):
                if j < board_size:
                    if board[X_MAX][j] == "*":
                        X_MAX += 1
                        break
                    elif board[X_MAX - 1][j] == "*":
                        found = True
            else:
                if not found:
                    X_MAX -= 1

        if Y_MIN > 0:  # get new y_min
            found: bool = False

            for j in range(X_MIN, Y_MAX + 1):
                if j < board_size:
                    if board[j][Y_MIN] == "*":
                        Y_MIN -= 1
                        break
                    elif board[j][Y_MIN + 1] == "*":
                        found = True
            else:
                if not found:
                    Y_MIN += 1
        if Y_MAX < board_size - 1:  # get new y_max
            found: bool = False

            for j in range(X_MIN, X_MAX + 1):
                if j < board_size:
                    if board[j][Y_MAX] == "*":
                        Y_MAX += 1
                        break
                    elif board[j][Y_MAX - 1] == "*":
                        found = True
            else:
                if not found:
                    Y_MAX -= 1


def print_board(board: list) -> None:
    global X_MIN, X_MAX, Y_MIN, Y_MAX

    for i in range(min(X_MIN, Y_MIN), max(X_MAX, Y_MAX) + 1):
        for j in range(min(X_MIN, Y_MIN), max(X_MAX, Y_MAX) + 1):
            print(board[i][j], end=" ")
        print()
    print()


def get_neighbour_count(board: list, x: int, y: int, board_size: int) -> int:
    count = 0

    for i in range(max(x - 1, 0), min(x + 2, board_size)):
        for j in range(max(y - 1, 0), min(y + 2, board_size)):
            if (i, j) != (x, y) and board[i][j] == "*":
                count += 1

    return count


def fill_neighbors_array(board: list, neighbours, cell: list, board_size: int) -> list:
    global X_MIN, X_MAX, Y_MIN, Y_MAX

    for x in range(X_MIN, X_MAX + 1):
        for y in range(Y_MIN, Y_MAX + 1):
            neighbours[x][y] = get_neighbour_count(board, x, y, board_size)

    return neighbours


def get_new_state(
    board: list, neighbours: list, living_cells: list, board_size: int
) -> None:
    """
    Any live cell with less than two live neighbours dies.
    Any live cell with two or three live neighbours remains living.
    Any live cell with more than three live neighbours dies.
    Any dead cell with exactly three live neighbours becomes a live cell.
    A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
    """
    global X_MIN, X_MAX, Y_MIN, Y_MAX
    neighbours = fill_neighbors_array(board, neighbours, living_cells, board_size)

    for x in range(X_MIN, X_MAX + 1):
        for y in range(Y_MIN, Y_MAX + 1):
            if neighbours[x][y] < 2:
                board[x][y] = "."
            elif neighbours[x][y] == 3:
                board[x][y] = "*"
            elif neighbours[x][y] > 3:
                board[x][y] = "."

    update_range(board, board_size)


def conway_game_of_life(living_cells: list, board_size: int, steps: int) -> None:
    """
    Time Complexity: O(steps*board_size*board_size)
    Space Complexity: O(board_size*board_size)
    """
    global X_MIN, X_MAX, Y_MIN, Y_MAX
    board: list = [["."] * board_size for _ in range(board_size)]
    neighbours: list = [[0] * board_size for _ in range(board_size)]
    X_MIN, X_MAX, Y_MIN, Y_MAX = 100, 0, 100, 0

    for x, y in living_cells:
        board[x][y] = "*"

    update_range(board, board_size, True)

    for _ in range(steps):
        get_new_state(board, neighbours, living_cells, board_size)
        print_board(board)


if __name__ == "__main__":
    print("Glider: period 4")
    conway_game_of_life([(3, 3), (4, 4), (3, 5), (4, 5), (5, 4)], 10, 8)
    print("Blinker: period 2")
    conway_game_of_life([(3, 5), (4, 5), (5, 5)], 10, 8)
    print("Toad: period 2")
    conway_game_of_life([(2, 1), (3, 1), (4, 2), (1, 3), (2, 4), (3, 4)], 10, 8)
    print("beehive: still life")
    conway_game_of_life([(2, 1), (1, 2), (1, 3), (2, 4), (3, 2), (3, 3)], 10, 8)
