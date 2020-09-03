"""
Given a string, write an algorithm to find the longest substring with at most two characters.
"""
from collections import defaultdict


def longest_substr(text: str, max_unique: int) -> str:
    """
    O(n) & O(n)
    """
    char_count = defaultdict(int)
    unique_chars = set()
    start, end = 0, 0
    substr = ""
    len_max = 0

    for index, char in enumerate(text):
        if len(unique_chars) == max_unique and char not in unique_chars:
            if end - start + 1 > len_max:
                len_max = end - start + 1
                substr = text[start: end + 1]

            while start < end:
                char_count[text[start]] -= 1
                start += 1

                if char_count[text[start - 1]] == 0:
                    unique_chars.remove(text[start - 1])
                    break

        char_count[char] += 1
        unique_chars.add(char)
        end = index

    if end - start + 1 > len_max:
        substr = text[start: end + 1]

    return substr


if __name__ == "__main__":
    assert longest_substr("aabbccddc", 2) == "ccddc"
    assert longest_substr("aabacbeeeebeaabb", 2) == "beeeebe"
    assert longest_substr("aaaaaa", 2) == "aaaaaa"
