"""
Given a start word, an end word, and a dictionary of valid words,
find the shortest transformation sequence from start to end
such that only one letter is changed at each step of the sequence,
and each transformed word exists in the dictionary.
If there is no possible transformation, return null.
Each word in the dictionary have the same length as start and end and is lowercase.

For example,
    given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"},
    return ["dog", "dot", "dat", "cat"].

Given
    start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"},
    return null as there is no possible transformation from dog to cat.
"""
from typing import List, Optional


def can_transform(word_1: str, word_2: str) -> bool:
    count_diff = 0

    for c1, c2 in zip(word_1, word_2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 1:
                return False
    return count_diff < 2


def _transform(
    cur: str, end: str, dictionary: set, visited: set
) -> Optional[List[str]]:
    """
    Backtracking
    Time Complexity: O(2^n)
    """
    if cur == end:
        return [cur]

    for word in dictionary:
        if word not in visited and can_transform(cur, word):
            visited.add(word)
            words = _transform(word, end, dictionary, visited)

            if words:
                return [cur] + words

            visited.remove(word)

    return None


def transformation_seq(start: str, end: str, dictionary: set) -> Optional[List[str]]:
    return _transform(start, end, dictionary, set())


if __name__ == "__main__":
    assert transformation_seq("dog", "cat", {"dot", "dop", "dat", "cat"}) == [
        "dog",
        "dot",
        "dat",
        "cat",
    ]
    assert transformation_seq("dog", "cat", {"dot", "tod", "dat", "dar"}) is None
