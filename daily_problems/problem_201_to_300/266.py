"""
A step word is formed by taking a given word,
adding a letter, and anagramming the result.
For example, starting with the word "APPLE",
you can add an "A" and anagram to get "APPEAL".
Given a dictionary of words and an input word,
create a function that returns all valid step words.
"""
from collections import defaultdict
from typing import List


def can_convert(chars: dict, word: str) -> bool:
    char_count = defaultdict(int)
    miss = 0

    for char in word:
        if char in chars:
            char_count[char] += 1
        else:
            miss += 1

        if char_count[char] > chars[char]:
            miss += 1

    if miss > 1:
        return False
    return True


def step_words(words: List[str], input_word: str) -> List[str]:
    size = len(input_word)
    chars = defaultdict(int)
    res = []

    for char in input_word:
        chars[char] += 1

    for word in words:
        if len(word) == size + 1 and can_convert(chars, word):
            res.append(word)

    return res


if __name__ == "__main__":
    word_list = ["APPEAL", "AAPPLES", "BEATLES", "BEETLES", "BEELLES"]
    assert step_words(word_list, "APPLE") == ["APPEAL"]
    assert step_words(word_list, "TELEBS") == ["BEATLES", "BEETLES"]
