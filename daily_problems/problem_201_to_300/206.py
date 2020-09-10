"""
A permutation can be specified by an array P,
where P[i] represents the location of the element at i in the permutation.
For example,
    [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
Given an array and a permutation, apply the permutation to the array.
For example,
    given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""
from typing import List


def get_original(arr: List[str], perm: List[int]) -> List[str]:
    index = 0
    size = len(arr)

    while index < size:
        j = index

        while perm[j] != j:
            temp_j, temp_p = j, perm[j]
            perm[temp_p], perm[temp_j] = perm[temp_j], perm[temp_p]
            arr[temp_p], arr[temp_j] = arr[temp_j], arr[temp_p]

        index += 1

    return arr


if __name__ == "__main__":
    assert get_original(["c", "a", "b"], [2, 0, 1]) == ["a", "b", "c"]
