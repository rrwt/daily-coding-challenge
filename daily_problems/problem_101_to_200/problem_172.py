"""
Given a string s and a list of words words, where each word is the same length,
find all starting indices of substrings in s that is a concatenation of every
word in words exactly once.
For example,
    given s = "dogcatcatcodecatdog" and words = ["cat", "dog"],
    return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

    Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return []
    since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""
from typing import List
from itertools import permutations


def get_indices(text: str, words: List[str]) -> List[int]:
    words = ["".join(_) for _ in permutations(words)]
    indices = [text.find(word) for word in words]
    return [index for index in indices if index > -1]


if __name__ == "__main__":
    assert get_indices("dogcatcatcodecatdog", ["dog", "cat"]) == [0, 13]
    assert get_indices("barfoobazbitbyte", ["dog", "cat"]) == []
