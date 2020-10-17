"""
Connect 4 is a game where opponents take turns dropping
red or black discs into a 7 x 6 vertically suspended grid.
The game ends either when one player creates a line of four
consecutive discs of their color (horizontally, vertically,
or diagonally), or when there are no more spots left in the
grid. Design and implement Connect 4.
"""


class Connect4:
    def __init__(self):
        self.board = [[""] * 7 for _ in range(6)]
        self.turn = "red"
        self.finished = False
        self.num_turns = 0
        self._winner = None

    @property
    def winner(self):
        return self._winner

    def _check_horizontally(self, row: int, column: int) -> bool:
        count_consecutive = 0

        for x in range(max(row - 3, 0), min(row + 4, 7)):
            if self.board[x][column] == self.turn:
                count_consecutive += 1

                if count_consecutive == 4:
                    self._winner = self.turn
                    return True
            else:
                count_consecutive = 0

        return False

    def _check_vertically(self, row: int, column: int) -> bool:
        count_consecutive = 0

        for y in range(max(column - 3, 0), min(column + 4, 6)):
            if self.board[row][y] == self.turn:
                count_consecutive += 1

                if count_consecutive == 4:
                    self._winner = self.turn
                    return True
            else:
                count_consecutive = 0

        return False

    def _check_first_diagonal(self, row: int, column: int) -> bool:
        count_consecutive = 0

        for diff in range(-3, 4):
            if 0 <= row + diff < 7 and 0 <= column + diff < 6:
                if self.board[row + diff][column + diff] == self.turn:
                    count_consecutive += 1

                    if count_consecutive == 4:
                        self._winner = self.turn
                        return True
                else:
                    count_consecutive = 0
            else:
                count_consecutive = 0

        return False

    def _check_second_diagonal(self, row: int, column: int) -> bool:
        count_consecutive = 0

        for diff in range(-3, 4):
            if 0 <= row + diff < 7 and 0 <= column - diff < 6:
                if self.board[row + diff][column + diff] == self.turn:
                    count_consecutive += 1

                    if count_consecutive == 4:
                        self._winner = self.turn
                        return True
                else:
                    count_consecutive = 0
            else:
                count_consecutive = 0

        return False

    def game_ended(self, row: int, column: int) -> bool:
        if self.num_turns < 7:
            return False

        # horizontal
        if self._check_horizontally(row, column):
            return True

        # vertical
        if self._check_vertically(row, column):
            return True

        # first diagonal
        if self._check_first_diagonal(row, column):
            return True

        # second diagonal
        if self._check_second_diagonal(row, column):
            return True

        return self.num_turns == 42

    def play(self, column: int) -> bool:
        """
        :return: Whether the game ended or not
        """
        if self.finished:
            raise Exception("Cannot play without resetting the board")

        for row in range(6):
            if self.board[row][column] == "":
                self.board[row][column] = self.turn
                self.num_turns += 1

                if self.game_ended(row, column):
                    self.finished = True
                break
        else:
            print(f"Cannot put more disks in column {column}")
            return True

        return self.finished
