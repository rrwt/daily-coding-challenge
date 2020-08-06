"""
Given a list of possibly overlapping intervals, return a new list
of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.
For example,
    given [(1, 3), (5, 8), (4, 10), (20, 25)],
    you should return [(1, 3), (4, 10), (20, 25)].
"""


def overlapping_intervals(intervals: list) -> list:
    length = len(intervals)

    if length < 2:
        return intervals

    intervals.sort(key=lambda _: _[0])  # sort by starting interval

    return_list = [intervals[0]]

    for i in range(1, length):
        for j, tup in enumerate(return_list):
            if intervals[i][0] <= tup[1]:
                return_list[j] = (tup[0], max(tup[1], intervals[i][1]))
                break
        else:
            return_list.append(intervals[i])

    return return_list


if __name__ == "__main__":
    print(overlapping_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))
    print(overlapping_intervals([(1, 3), (5, 8), (2, 10), (10, 25)]))
    print(overlapping_intervals([(0, 3)]))
    print(overlapping_intervals([(1, 2), (3, 8), (4, 6), (20, 25)]))
