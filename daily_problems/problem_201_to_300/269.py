"""
You are given an string representing the initial conditions of some dominoes.
Each element can take one of three values:
    L, meaning the domino has just been pushed to the left,
    R, meaning the domino has just been pushed to the right, or
    ., meaning the domino is standing still.

Determine the orientation of each tile when the dominoes stop falling.
Note that if a domino receives a force from the left and right side
simultaneously, it will remain upright.
For example,
    given the string .L.R....L, you should return LL.RRRLLL.
    Given the string ..R...L.L, you should return ..RR.LLLL
"""


def get_orientation(tiles: str) -> str:
    size = len(tiles)
    tiles = list(tiles)

    for _ in range(size - 1):
        changed_indexes = set()

        for index, tile in enumerate(tiles):
            if tile == ".":
                direction = 0

                if (
                    index > 0
                    and tiles[index - 1] == "R"
                    and index - 1 not in changed_indexes
                ):
                    direction += 1
                if (
                    index < size - 1
                    and tiles[index + 1] == "L"
                    and index + 1 not in changed_indexes
                ):
                    direction -= 1

                if direction != 0:
                    changed_indexes.add(index)

                if direction > 0:
                    tiles[index] = "R"
                elif direction < 0:
                    tiles[index] = "L"

        if not changed_indexes:
            break

    return "".join(tiles)


if __name__ == "__main__":
    assert get_orientation(".L.R....L") == "LL.RRRLLL"
    assert get_orientation("..R...L.L") == "..RR.LLLL"
