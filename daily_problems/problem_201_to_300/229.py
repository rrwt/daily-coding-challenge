"""
Snakes and Ladders is a game played on a 10 x 10 board,
the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move
forward a number of spaces equal to the result.
If they land on a square that represents a snake or ladder,
they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to play snakes and ladders.
For convenience, here are the squares representing snakes and ladders, and their outcomes:
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
"""
import sys


class SnakesAndLadders:
    def __init__(self, snakes: dict, ladders: dict, width: int = 10, height: int = 10):
        self.snakes = snakes
        self.ladders = ladders
        self.index = 0
        self.end = width * height
        self.cache = {}

    def min_turns(self, index: int = 0) -> int:
        """
        At every ladder, we either take it or leave it.
        Always try to move 6 steps, except when
            1. There is a ladder (before n = 6)
            2. There is a snake (at n=6)
        """
        if index >= self.end:
            return 0

        if index in self.cache:
            return self.cache[index]

        turns = sys.maxsize

        for next_block in range(index + 1, index + 7):
            if next_block in self.ladders and next_block not in self.cache:
                turns = min(turns, 1 + self.min_turns(self.ladders[next_block]))

        for next_block in range(index + 6, index, -1):
            if next_block not in self.snakes:
                turns = min(turns, 1 + self.min_turns(next_block))
                break

        self.cache[index] = turns
        return turns


if __name__ == "__main__":
    sn = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    la = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    sal = SnakesAndLadders(sn, la)
    print(sal.min_turns())