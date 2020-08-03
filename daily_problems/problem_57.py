"""
Given a string s and an integer k, break up the string into multiple lines
such that each line has a length of k or less. You must break it up so that
words don't break across lines. Each line has to have the maximum possible
amount of words. If there's no way to break the text up, then return null.
You can assume that there are no spaces at the ends of the string and that
there is exactly one space between each word.
For example,
    given the string "the quick brown fox jumps over the lazy dog" and k = 10,
    you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
    No string in the list has a length of more than 10.
"""
from typing import List, Optional


def word_break(text: str, k: int) -> Optional[List[str]]:
    words = text.split(" ")
    index = 0
    length = len(words)
    return_list = []

    while index < length:
        cur_len = len(words[index])
        start = index
        index += 1

        while index < length and cur_len + 1 + len(words[index]) <= k:
            cur_len += 1 + len(words[index])
            index += 1

        if start == index or cur_len > k:
            return None

        return_list.append(" ".join(words[start: index]))

    return return_list


if __name__ == "__main__":
    print(word_break("the quick brown fox jumps over the lazy dog", 10), sep="\n")
    print(word_break("the encyclopedia britannica", 11), sep="\n")
