"""
You are given n activities (sorted by finish time) with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.
"""


def max_activities(start: list, end: list) -> int:
    """
    Since the activities are sorted by finish time, we can solve the problem in O(n) time
    """
    return_value: int = 1
    index: int = 1
    length: int = len(start)
    prev_index: int = 0

    while index < length:
        if start[index] >= end[prev_index]:
            return_value += 1
            prev_index = index
        index += 1

    return return_value


if __name__ == "__main__":
    assert max_activities([10, 12, 20], [20, 25, 30]) == 2
    assert max_activities([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]) == 4
