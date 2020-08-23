"""KMP algorithm
"""

from typing import List


def generate_lps(pattern: str, length: int) -> List[int]:
    """
    Generate longest proper prefix which is also a suffix
    """
    index = 1
    lps: List[int] = [0] * length
    cur_len = 0

    while index < length:
        if pattern[index] == pattern[cur_len]:
            cur_len += 1
            lps[index] = cur_len
            index += 1
        elif cur_len != 0:
            cur_len = lps[cur_len - 1]
        else:
            index += 1

    return lps


def kmp(text: str, pattern: str) -> List[int]:
    l_text: int = len(text)
    l_pat: int = len(pattern)

    lps: List[int] = generate_lps(pattern, l_pat)

    index_text, index_pat = 0, 0
    return_list: List[int] = []

    while index_text < l_text:
        if text[index_text] == pattern[index_pat]:
            index_text += 1
            index_pat += 1

            if index_pat == l_pat:
                return_list.append(index_text - l_pat)
                index_pat = lps[index_pat - 1]
        elif index_pat > 0:
            index_pat = lps[index_pat - 1]
        else:
            index_text += 1

    return return_list


if __name__ == "__main__":
    print(kmp("AAAAABAAABA", "AAAA"))
    print(kmp("AAAAABAAACAAAAA", "AAACAAAA"))
    print(kmp("ABABDABACDABABCABAB", "ABABCABAB"))
