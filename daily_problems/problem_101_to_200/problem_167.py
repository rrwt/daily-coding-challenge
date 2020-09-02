"""
Given a list of words, find all pairs of unique indices
such that the concatenation of the two words is a palindrome.
For example,
    given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""
from typing import List, Tuple


def is_palindrome(word: str) -> bool:
    i, j = 0, len(word) - 1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1

    return True


def unique_indices(words: List[str]) -> List[Tuple[int, int]]:
    """
    Time Complexity: O(n * n * n)
    """
    processed = set()
    indices = []

    for i, word_1 in enumerate(words):
        for j, word_2 in enumerate(words):
            if i == j:
                continue

            word = word_1 + word_2

            if word not in processed and is_palindrome(word_1 + word_2):
                indices.append((i, j))
                processed.add(word)

    return indices


if __name__ == "__main__":
    assert unique_indices(["code", "edoc", "da", "d"]) == [(0, 1), (1, 0), (2, 3)]
