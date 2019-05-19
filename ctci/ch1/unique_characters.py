"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures
"""

# time: O(n), space: O(n)
def using_hash_table(str_in):
    d = {}

    for c in str_in:
        if c in d:
            return False
        else:
            d[c] = 1

    return True


# time: O(nlog(n)), space: O(1)
def without_using_additional_data_structures(str_in):
    str_in.sort()

    for ind in range(0, len(str_in) - 1):
        if str_in[ind] == str_in[ind + 1]:
            return False

    return True
