"""
Given a string and a pattern, find the starting indices of all occurrences
of the pattern in the string. For example,
    given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""
from typing import List


def longest_proper_prefix(pattern: str, length: int) -> List[int]:
    lps = [0] * length
    index = 1
    j = 0

    while index < length:
        if pattern[index] == pattern[j]:
            lps[index] = lps[index - 1] + 1
            index += 1
            j += 1
        elif j > 0:
            j = lps[j - 1]
        else:
            index += 1

    return lps


def pattern_search(text: str, pat: str) -> List[int]:
    """
    KMP Pattern search algorithm
    """
    len_text = len(text)
    len_pat = len(pat)
    lps = longest_proper_prefix(pat, len_pat)
    in_txt = 0
    in_pat = 0
    indexes = []

    while in_txt < len_text:
        if text[in_txt] == pat[in_pat]:
            in_txt += 1
            in_pat += 1

            if in_pat == len_pat:
                indexes.append(in_txt - in_pat)
                in_pat = lps[in_pat - 1]
        elif in_pat > 0:
            in_pat = lps[in_pat - 1]
        else:
            in_txt += 1

    return indexes


if __name__ == "__main__":
    assert pattern_search("abracadabra", "abr") == [0, 7]
    assert pattern_search("aabaacaabaac", "aacaab") == [3]
