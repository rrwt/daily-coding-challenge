"""
A teacher must divide a class of students into two teams to play dodge ball.
Unfortunately, not all the kids get along, and several refuse to be put on
the same team as that of their enemies.
Given an adjacency list of students and their enemies, write an algorithm
that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.
    students = { 0: [3], 1: [2], 2: [1, 4], 3: [0, 4, 5], 4: [2, 3], 5: [3] }

On the other hand, given the input below, you should return False.
    students = {0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4, 5], 4: [2, 3], 5: [3] }
"""
from typing import Union, Tuple, Set


def dfs(src: int, students: dict, first_team: Set, second_team: Set) -> bool:
    enemy_in_first = enemy_in_second = False

    for enemy in students[src]:
        if enemy in first_team:
            enemy_in_first = True
        elif enemy in second_team:
            enemy_in_second = True

    if enemy_in_first and enemy_in_second:
        return False
    elif enemy_in_first:
        second_team.add(src)
    else:
        first_team.add(src)

    for enemy in students[src]:
        if enemy not in first_team and enemy not in second_team:
            res = dfs(enemy, students, first_team, second_team)
            if res is False:
                return False

    return True


def partition(students: dict) -> Union[Tuple[Set, Set], bool]:
    num_students = len(students)
    first_team = set()
    second_team = set()
    next_student = 0

    while len(first_team) + len(second_team) < num_students:
        if dfs(next_student, students, first_team, second_team) is False:
            return False
        next_student += 1

    return first_team, second_team


if __name__ == "__main__":
    assert partition({0: [3], 1: [2], 2: [1, 4], 3: [0, 4, 5], 4: [2, 3], 5: [3]}) == (
        {0, 1, 4, 5},
        {2, 3},
    )
    assert (
        partition({0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4, 5], 4: [2, 3], 5: [3]})
        is False
    )
