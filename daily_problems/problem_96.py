"""
Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""
from typing import List, Optional


def get_permutations(numbers: Optional[List[int]] = None) -> List[List[int]]:
    if not numbers:
        return [[]]

    permutations = []

    for index, number in enumerate(numbers):
        sub_perms = get_permutations(numbers[:index] + numbers[index+1:])

        for sub_perm in sub_perms:
            permutations.append(sub_perm + [number])

    return permutations


if __name__ == "__main__":
    print(get_permutations([1, 2, 3]))
