"""
Given a string with repeated characters, rearrange the string so that no
two adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""
from collections import defaultdict
from typing import Optional


def rearrange_duplicate_char(text: str) -> Optional[str]:
    index = 0
    size = len(text)
    chars = list(text)

    while index < size - 1:
        j = index + 1

        while j < size and chars[j] == chars[index]:
            j += 1

        if index + 1 < j < size:
            index += 1
            chars[index], chars[j] = chars[j], chars[index]
        elif j == index + 1:
            index += 1
        else:
            return None

    return "".join(chars)


if __name__ == "__main__":
    assert rearrange_duplicate_char("aaabbc") == "ababac"
    assert rearrange_duplicate_char("aaab") is None
