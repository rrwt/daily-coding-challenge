"""
Determine whether there exists a one-to-one character
mapping from one string s1 to another s2.
For example,
    given s1 = abc and s2 = bcd, return true
    since we can map a to b, b to c, and c to d.

    Given s1 = foo and s2 = bar, return false
    since the o cannot map to two characters.
"""
from collections import defaultdict


def map_chars(text_1: str, text_2: str) -> bool:
    """
    In case the distribution is random
    """
    if len(text_1) != len(text_2):
        return False

    d_1 = defaultdict(int)
    d_2 = defaultdict(int)

    for c in text_1:
        d_1[c] += 1

    for c in text_2:
        d_2[c] += 1

    values_1 = list(d_1.values())
    values_2 = list(d_2.values())

    for index, value in enumerate(values_1):
        for index_2, value_2 in enumerate(values_2):
            if value == value_2:
                values_1[index] = -1
                values_2[index_2] = -1
                break
        else:
            return False

    for index, value in enumerate(values_2):
        if value != -1:
            return False

    return True


def map_chars_one_to_one(text_1: str, text_2: str) -> bool:
    """
    in case the mapping is direct
    """
    char_dict = {}

    for c1, c2 in zip(text_1, text_2):
        if c1 not in char_dict:
            char_dict[c1] = c2
        elif char_dict[c1] != c2:
            return False

    return True


if __name__ == "__main__":
    assert map_chars("abc", "bcd") is True
    assert map_chars("foo", "bar") is False

    assert map_chars_one_to_one("abc", "bcd") is True
    assert map_chars_one_to_one("foo", "bar") is False
