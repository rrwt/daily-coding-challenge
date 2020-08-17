"""
Given a string and a set of characters,
return the shortest substring containing all the characters in the set.

For example,
    given the string "figehaeci" and the set of characters {a, e, i},
    you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
from collections import defaultdict
from typing import Optional


def shortest_substring_containing_characters(text: str, char_set: set) -> Optional[str]:
    """
    O(n) & O(k)
    """
    start = 0
    end = -1
    count_char = defaultdict(int)  # char and its count
    found_set = set()

    for index, char in enumerate(text):
        if char in char_set:
            count_char[char] += 1
            found_set.add(char)

            if len(found_set) == len(char_set):
                new_start = start
                new_end = index

                while text[new_start] not in char_set or count_char[text[new_start]] > 1:
                    if text[new_start] in count_char:
                        count_char[text[new_start]] -= 1

                    new_start += 1

                if end < start or (new_end - new_start) < (end - start):
                    end = new_end
                    start = new_start

    return text[start: end + 1] if end > start else None


if __name__ == '__main__':
    assert shortest_substring_containing_characters("figehaeci", {"a", "e", "i"}) == "aeci"
    assert shortest_substring_containing_characters("abcdefgh", {"a", "e", "n"}) is None
