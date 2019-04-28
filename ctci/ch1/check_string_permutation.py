"""
Given two strings,
write a method to decide if one is a permutation of the other.
"""
from collections import defaultdict


# time: O(n), space: O(n)
def check_permutation(str1, str2):
    """
    using dictionary.
    Can also be done using arrays in case we know the character range
    """
    if len(str1) != len(str2):
        return False

    d = defaultdict(int)

    for k in str1:
        d[k] += 1

    for k in str2:
        if k not in d or d[k] == 0:
            return False
        else:
            d[k] -= 1

    return True


if __name__ == "__main__":
    print(check_permutation("asdfghjkla", "sadfhglkja"))
