"""
Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character
of X is same as the first character of Y.
For example,
    the words ['chair', 'height', 'racket', 'touch', 'tunic']
    can form the following circle:
    chair --> racket --> touch --> height --> tunic --> chair.
"""
from collections import defaultdict
from typing import List


def _can_form_a_circle(words: set, first: str, prev: str) -> bool:
    if not words:
        if prev[-1] == first[0]:
            return True
        return False

    for word in words:
        if word[0] == prev[-1]:
            if _can_form_a_circle(words - {word}, first, word):
                return True

    return False


def can_form_a_circle(words: List[str]) -> bool:
    hashmap = defaultdict(int)

    for word in words:
        hashmap[word[0]] += 1
        hashmap[word[-1]] += 1

    for value in hashmap.values():
        if value < 2:
            return False

    words = set(words)

    for word in words:
        if _can_form_a_circle(words - {word}, word, word):
            return True

    return False


if __name__ == "__main__":
    assert can_form_a_circle(["chair", "height", "racket", "touch", "tunic"]) is True
