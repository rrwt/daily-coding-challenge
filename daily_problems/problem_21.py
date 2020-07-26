"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from typing import List


def min_rooms(intervals: List[tuple]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])  # sort by end time
    rooms: int = 1
    j: int = 0

    for i in range(1, len(intervals)):
        while j < i and intervals[j][1] < intervals[i][0]:
            j += 1

        rooms = max(rooms, i - j + 1)

    return rooms


def min_rooms_alt(intervals: List[tuple]) -> int:
    # alternative solution.
    intervals.sort(key=lambda tup: tup[1])  # sort by end time
    count = 0
    previous = -1

    for (start, end) in intervals:
        if start >= previous:
            count += 1
            previous = end

    return count


if __name__ == "__main__":
    first: List[tuple] = [(30, 75), (0, 50), (60, 150)]
    print("min rooms for", first, "are:", min_rooms(first))
    print("min rooms for", first, "are:", min_rooms_alt(first))

    second: List[tuple] = [
        (900, 910),
        (940, 1200),
        (950, 1120),
        (1100, 1130),
        (1500, 1900),
        (1800, 2000),
    ]
    print("min room for", second, "are:", min_rooms(second))
    print("min room for", second, "are:", min_rooms_alt(second))

    assert min_rooms([]) == min_rooms_alt([]) == 0
