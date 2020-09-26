"""
Write a function, throw_dice(N, faces, total), that determines
how many ways it is possible to throw N dice with some number
of faces each to get a specific total.
For example, throw_dice(3, 6, 7) should equal 15.
"""


def throw_dice(num_dices: int, num_faces: int, total: int) -> int:
    if total <= 0 or num_dices <= 0:
        return 0
    if total == 1 and num_dices == 1:
        return 1
    if num_dices == 1:
        return 1 if total <= num_faces else 0

    count = 0

    for num in range(1, num_faces + 1):
        count += throw_dice(num_dices - 1, num_faces, total - num)

    return count


if __name__ == "__main__":
    assert throw_dice(3, 6, 7) == 15
