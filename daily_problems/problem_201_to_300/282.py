"""
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
"""
import math
from typing import List


def pythagorean_triplets(arr: List[int]) -> bool:
    size = len(arr)
    arr.sort()

    for i in range(size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if arr[i] + arr[j] > arr[k]:
                    if math.pow(arr[i], 2) + math.pow(arr[j], 2) == math.pow(arr[k], 2):
                        return True
                else:
                    break

    return False


if __name__ == "__main__":
    assert pythagorean_triplets([1, 2, 3, 4, 5]) is True
