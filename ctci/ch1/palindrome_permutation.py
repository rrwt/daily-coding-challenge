"""
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""
import collections


def is_permutation_palindrome(str_in):
    str_in = "".join(str_in.strip().split())
    d = collections.defaultdict(int)
    l = len(str_in)

    tolerance = l % 2

    for s in str_in:
        d[s.lower()] += 1

    for v in d.values():
        if v % 2 == 1 and not tolerance:
            return False
    return True


if __name__ == "__main__":
    print(is_permutation_palindrome("Tact Coa"))
