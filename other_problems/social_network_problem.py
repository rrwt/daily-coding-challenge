"""
There are N people in a social network and there are friends group.
Each person can be part of a friend group of a specific size.
Number of people in the social network – N
An array of size N specifying group size for each person. – (g0, g2, g3,….., gn).
The first person (at index 0) is part of a friend group of maximum size g0,
the second person(at index 1) is part of a friend group of maximum size g2 and so on.
Objective:
    Write an algorithm to create the minimum number of friend groups so that
    each person can be put into one of these groups as per the given group
    size of each person.
Output:
    Print minimum no of groups and persons assigned to each group.
"""
from collections import defaultdict, deque
from typing import Tuple, List, Deque


def get_group_people(group_sizes) -> Deque[Tuple]:
    groups_people = defaultdict(deque)

    for person, group_size in enumerate(group_sizes):
        groups_people[group_size].append(person)

    return deque(sorted(groups_people.items()))


def min_groups(group_sizes: List[int]) -> List[List[int]]:
    num_people = len(group_sizes)

    if num_people == 0:
        return [[]]
    if num_people == 1:
        return [[0]]

    groups_of_people = get_group_people(group_sizes)
    groups = []
    cur_group = []
    previous_group_size = 0

    while groups_of_people:
        group_size, people = groups_of_people.popleft()

        while people and len(cur_group) < previous_group_size:
            cur_group.append(people.popleft())

        if not people:
            continue

        if cur_group and len(cur_group) == previous_group_size:
            groups.append(cur_group)
            cur_group = []

        if people and not cur_group:
            while people:
                cur_group.append(people.popleft())

                if len(cur_group) == group_size:
                    groups.append(cur_group)
                    cur_group = []

        previous_group_size = group_size if cur_group else 0

    if cur_group:
        groups.append(cur_group)

    return groups


if __name__ == "__main__":
    assert min_groups([3, 3, 3, 3, 3, 1, 3]) == [[5], [0, 1, 2], [3, 4, 6]]
    assert min_groups([3, 2]) == [[1, 0]]
    assert min_groups([3, 2, 3, 3, 2, 2, 3, 2, 6]) == [
        [1, 4],
        [5, 7],
        [0, 2, 3],
        [6, 8],
    ]
