"""
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k,
write a program that searches for the pattern in the string
with less than O(N * k) worst-case time complexity.
If the pattern is found, return the start index of its location.
If not, return False.
"""
from typing import Optional, List


def longest_proper_prefix(pattern: str, len_pat: int) -> List[int]:
    lps = [0] * len_pat
    j = 0
    index = 1

    while index < len_pat:
        if pattern[index] == pattern[j]:
            lps[index] = lps[index-1] + 1
            index += 1
            j += 1
        elif j > 0:
            j = lps[j-1]
        else:
            index += 1

    return lps


def kmp(text: str, pattern: str) -> Optional[int]:
    len_pat = len(pattern)
    len_txt = len(text)
    lps = longest_proper_prefix(pattern, len_pat)
    ind_txt = 0
    ind_pat = 0

    while ind_txt < len_txt:
        if text[ind_txt] == pattern[ind_pat]:
            ind_txt += 1
            ind_pat += 1

            if ind_pat == len_pat:
                return ind_txt - ind_pat
        elif ind_pat > 0:
            ind_pat = lps[ind_pat-1]
        else:
            ind_txt += 1

    return None


if __name__ == "__main__":
    assert kmp("abracadabra", "abr") == 0
    assert kmp("aabaacaabaac", "aacaab") == 3
