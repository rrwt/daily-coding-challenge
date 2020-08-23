"""
Write a function that rotates a list by k elements.
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""
from typing import List, Tuple


def get_rotated_list(values: List[int], k: int) -> List[int]:
    """
    Copying original list
    O(n) and O(n)
    """
    len_val = len(values)
    k %= len_val

    return values[k:] + values[:k]


def get_rotated_list_without_extra_space(
    values: List[int], k: int
) -> Tuple[List[int], int]:
    """
    :returns: Tuple of number of move operations and List of values at new position
    """
    len_val = len(values)
    k %= len_val

    # number of rotations to be performed
    num_rot = min(k, len_val - k)
    moves = 0

    for start_index in range(num_rot):
        cur_index = start_index
        cur_val = values[start_index]

        while True:
            new_index = cur_index - k
            new_index = new_index + len_val if new_index < 0 else new_index
            values[new_index], cur_index, cur_val = (
                cur_val,
                new_index,
                values[new_index],
            )
            moves += 1

            if cur_index == start_index:
                break

    return values, moves


if __name__ == "__main__":
    assert get_rotated_list([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]

    for _ in range(1, 6):
        nums = [1, 2, 3, 4, 5, 6]
        assert get_rotated_list_without_extra_space([1, 2, 3, 4, 5, 6], _) == (
            nums[_:] + nums[:_],
            6,
        )
