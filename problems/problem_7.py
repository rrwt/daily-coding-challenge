"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways
it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

code = {k+1: chr(v) for k, v in enumerate(range(97, 123, 1))}
print(code)


def count_mapping(str_arr: str):
    if str_arr.startswith('0'):
        return 0
    elif len(str_arr) == 1 or str_arr in ("10", "20"):
        return 1
    elif len(str_arr) == 2 and str_arr.endswith('0') and str_arr not in ("10", "20"):
        return 0

    count = 1 if int(str_arr) in code else 0

    for i in range(1, len(str_arr)):
        count += count_mapping(str_arr[0:i]) * count_mapping(str_arr[i:])

    return count
