"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways
it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

code = {k + 1: chr(v) for k, v in enumerate(range(97, 123, 1))}


def count_mapping(str_arr: str):
    def join_string_sets(first, second):
        res = set()

        if isinstance(first, str) and isinstance(second, str):
            res.add(first + second)
        elif isinstance(first, str):
            for word in second:
                res.add(first + word)
        elif isinstance(second, str):
            for word in first:
                res.add(word + second)
        else:
            for w1 in first:
                for w2 in second:
                    res.add(w1 + w2)

        return res

    def get_mappings(arr):
        if arr.startswith("0"):
            return None
        elif len(arr) == 1 or arr in ("10", "20"):
            return code[int(arr)]
        elif len(arr) == 2 and arr.endswith("0") and arr not in ("10", "20"):
            return None

        res = set()

        if int(arr) in code:
            res.add(code[int(arr)])

        for ind in range(1, len(arr)):
            first = get_mappings(arr[0:ind])
            second = get_mappings(arr[ind:])

            if first and second:
                res = res.union(join_string_sets(first, second))

        return res

    result: set = set()
    str_len = len(str_arr)

    for i in range(1, str_len + 1):
        f = get_mappings(str_arr[0:i])

        if i < str_len:
            s = get_mappings(str_arr[i:])

            if f and s:
                result = result.union(join_string_sets(f, s))
        elif f:
            if isinstance(f, set):
                result = result.union(f)
            else:
                result.add(f)

    return len(result)
