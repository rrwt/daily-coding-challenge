"""
Given a set of positive integers, find all its subsets.
The set can contain duplicate elements, so any repeated
subset should be considered only once in the output.
"""
from typing import List, Set


def _get_subsets(integers: str, index: int, size: int) -> Set[str]:
    if index == size:
        return {""}

    results = []

    for items in _get_subsets(integers, index+1, size):
        results += [items, integers[index] + items]

    return set(results)


def get_subsets(integers: List[int]) -> List[List[int]]:
    subsets = _get_subsets("".join([str(_) for _ in integers]), 0, len(integers))
    results = []

    for string in subsets:
        results.append([int(char) for char in string])

    return results


if __name__ == '__main__':
    print(get_subsets([1, 2, 2]))
