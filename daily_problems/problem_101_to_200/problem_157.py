"""
Given a string, determine whether any permutation of it is a palindrome.
For example,
    carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
    daily should return false, since there's no rearrangement that can form a palindrome.
"""
from collections import defaultdict


def has_palindrome(text: str) -> bool:
    counts = defaultdict(int)

    for char in text:
        counts[char] += 1

    num_odd = 0

    for count in counts.values():
        if count & 1:
            num_odd += 1
            if num_odd > 1:
                return False

    return True


if __name__ == "__main__":
    assert has_palindrome("carrace") is True
    assert has_palindrome("daily") is False
