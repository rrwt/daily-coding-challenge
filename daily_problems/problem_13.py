"""
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".
"""
from collections import defaultdict


def longest_substring(string: str, k: int) -> int:
    """
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    length: int = len(string)
    max_count = min(length, k)
    hash_map: defaultdict = defaultdict(int)
    cur_char_len: int = 0
    distinct_chars: int = 0
    starting_index: int = 0

    for index, char in enumerate(string):
        if hash_map[char] == 0 and distinct_chars >= k:
            while starting_index < index:
                # reduce count of all elements, while all elements have count > 0
                el = string[starting_index]
                hash_map[el] -= 1
                cur_char_len -= 1
                starting_index += 1

                if hash_map[el] == 0:
                    distinct_chars -= 1
                    break

        cur_char_len += 1

        if hash_map[char] == 0:
            distinct_chars += 1

        hash_map[char] += 1
        max_count = max(max_count, cur_char_len)

    return max_count


def longest_substring_alt(string: str, k: int) -> int:
    """
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    hash_map = {}
    distinct_chars = set()

    for index, char in enumerate(string[:k]):
        hash_map[char] = index
        distinct_chars.add(char)

    set_size = len(distinct_chars)
    max_len = curr_len = k

    for index, char in enumerate(string[k:], start=k):
        if char not in distinct_chars:
            if set_size == k:
                char_to_remove = string[index - k]
                distinct_chars.remove(char_to_remove)
                curr_len = index - 1 - hash_map[char_to_remove]
                set_size -= 1

            distinct_chars.add(char)
            set_size += 1

        hash_map[char] = index
        curr_len += 1
        max_len = max(max_len, curr_len)

    return max_len


if __name__ == "__main__":
    assert longest_substring("abcba", 2) == 3
    assert longest_substring_alt("abcba", 2) == 3
    assert longest_substring("aabacbebebe", 3) == 7
    assert longest_substring_alt("aabacbebebe", 3) == 7
    assert longest_substring("eceba", 3) == 4
    assert longest_substring_alt("eceba", 3) == 4
