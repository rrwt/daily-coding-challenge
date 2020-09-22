"""
Ghost is a two-person word game where players alternate appending letters to a word.
The first person who spells out a word, or creates a prefix for which there is no
possible continuation, loses. Here is a sample game:
    Player 1: g
    Player 2: h
    Player 1: o
    Player 2: s
    Player 1: t [loses]
Given a dictionary of words, determine the letters the first player
should start with, such that with optimal play they cannot lose.
For example,
    if the dictionary is ["cat", "calf", "dog", "bear"],
    the only winning start letter would be b.
"""
from collections import defaultdict
from typing import List


def ghost(words: List[str]) -> List[str]:
    word_dict = defaultdict(list)

    for word in words:
        word_dict[word[0]].append(word)

    winning_starts = []

    for first_char, word_list in word_dict.items():
        if all((len(word) % 2 == 0 for word in word_list)):
            winning_starts.append(first_char)

    return winning_starts


if __name__ == "__main__":
    assert ghost(["cat", "calf", "dog", "bear"]) == ["b"]
