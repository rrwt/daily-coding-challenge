"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways
it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def count_mapping(str_arr: str):
    if str_arr == '0':
        return 0
    elif len(str_arr) == 1 or str_arr in ("10", "20"):
        return 1

    return 2
