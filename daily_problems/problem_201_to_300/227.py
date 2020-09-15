"""
Boggle is a game played on a 4 x 4 grid of letters.
The goal is to find as many words as possible that can be formed
by a sequence of adjacent letters in the grid, using each cell at most once.
Given a game board and a dictionary of valid words, implement a Boggle solver.
"""
from typing import List, Tuple


class Boggle:
    def __init__(
        self, grid: List[List[str]], words: List[str], size_x: int = 4, size_y: int = 4
    ) -> None:
        self.grid = grid
        self.words = words
        self.size_x = size_x
        self.size_y = size_y

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbors = []

        for dif_x in (-1, 0, 1):
            for dif_y in (-1, 0, 1):
                if dif_x == 0 and dif_y == 0:
                    continue
                elif -1 < x + dif_x < self.size_x and -1 < y + dif_y < self.size_y:
                    neighbors.append((x + dif_x, y + dif_y))

        return neighbors

    def find_at_index(
        self, word, index: int, size: int, x: int, y: int, visited: set
    ) -> bool:
        if index == size:
            return True

        for nx, ny in self.get_neighbors(x, y):
            if (nx, ny) not in visited and word[index] == self.grid[nx][ny]:
                visited.add((nx, ny))
                found = self.find_at_index(word, index + 1, size, nx, ny, visited)

                if found:
                    return True
                visited.remove((nx, ny))

        return False

    def solve(self) -> int:
        count_found = 0

        for word in self.words:
            found = False
            for x in range(self.size_x):
                for y in range(self.size_y):
                    if self.grid[x][y] == word[0]:
                        found = self.find_at_index(word, 1, len(word), x, y, {(x, y)})
                        if found:
                            break
                if found:
                    break
            if found:
                count_found += 1

        return count_found


if __name__ == "__main__":
    b = Boggle(
        [
            ["t", "a", "n", "z"],
            ["j", "k", "v", "e"],
            ["s", "e", "r", "t"],
            ["e", "i", "h", "v"],
        ],
        ["etherise", "evert", "knaves", "sievert", "vena", "tries", "abracadabra"],
        4,
        4,
    )
    assert b.solve() == 6
