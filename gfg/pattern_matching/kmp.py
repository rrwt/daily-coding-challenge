"""KMP algorithm
"""

from typing import List


def generate_lps(pattern: str, length: int) -> List[int]:
    """
    Generate longest proper prefix which is also a suffix
    """
    index = 1
    lps: List[int] = [0] * length
    j = 0

    while index < length:
        if pattern[index] == pattern[j]:
            j += 1
            lps[index] = j
            index += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            index += 1

    return lps


def kmp(text: str, pattern: str) -> List[int]:
    l_text: int = len(text)
    l_pat: int = len(pattern)

    lps: List[int] = generate_lps(pattern, l_pat)

    index: int = 0
    return_list: List[int] = []

    j = 0

    while index < l_text:
        while index < l_text and j < l_pat and text[index] == pattern[j]:
            index += 1
            j += 1

        if j == l_pat:
            return_list.append(index - l_pat)

        if index < l_text and j > 0:
            j = lps[j - 1]
        else:
            index += 1

    return return_list


if __name__ == "__main__":
    print(kmp("AAAAABAAABA", "AAAA"))
    print(kmp("AAAAABAAACAAAAA", "AAACAAAA"))
    print(kmp("ABABDABACDABABCABAB", "ABABCABAB"))
