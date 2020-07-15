"""
Given an integer k and a string s, find the length of the longest substring that
contains at most k distinct characters.
For example, given s = "abcba" and k = 2,
the longest substring with k distinct characters is "bcb".
"""
from collections import deque, defaultdict


def longest_substring(string: str, k: int) -> int:
    """
    Time complexity: O(n)
    Space Complexity: O(n)
    """
    length: int = len(string)
    max_count = min(length, k)
    d: defaultdict = defaultdict(int)
    q_l: int = 0
    starting_index: int = 0

    for index, char in enumerate(string):
        if d[char] == 0 and q_l >= k:
            while starting_index < index:
                el = string[starting_index]
                d[el] -= 1
                q_l -= 1
                starting_index += 1
                if d[el] == 0:
                    break

        q_l += 1
        d[char] += 1
        max_count = max(max_count, q_l)

    return max_count


if __name__ == "__main__":
    print(longest_substring("abcba", 2))
    print(longest_substring("aabacbebebe", 3))
