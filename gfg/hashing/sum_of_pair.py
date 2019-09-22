"""
Given an array of integers and a number k, write a function that returns true
if given array can be divided into pairs such that sum of every pair is divisible by k.
"""
from collections import defaultdict


def sum_of_pairs(arr: list, k: int) -> bool:
    """
    even number of 0's in frequency means there is atleast a pair
    freq of element%k == k/2 and there are atleast 2 such elements means there is atleast a pair
    if exists, freq of element%k and freq of (k-element)%k means there is atleast a pair.
    """
    frequency: dict = defaultdict(int)

    for element in arr:
        frequency[element % k] += 1

    for element in arr:
        remainder = element % k
        if remainder == 0 and frequency[remainder] & 1:
            return False
        elif remainder == k / 2 and frequency[remainder] & 1:
            return False
        elif frequency[k - remainder] != frequency[remainder]:
            return False

    return True


if __name__ == "__main__":
    assert sum_of_pairs([92, 75, 65, 48, 45, 35], 10)
