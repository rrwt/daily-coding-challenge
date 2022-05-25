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


def get_cur_val(cur_val, next_val, dp, index) -> int:
    plus_2 = dp[index + 2] or 1

    if next_val == "0":
        # All the variations till + 2
        return plus_2
    elif 10 < int(cur_val + next_val) < 27:
        # All the variations till index + 2 and a two-digit number +
        # All the variations till index + 1 and a one-digit number
        return dp[index + 1] + plus_2

    # All the variations till + 1
    return dp[index + 1]


def count_mapping_dp(input_str: str) -> int:
    length = len(input_str)
    dp = [0] * (length + 1)
    dp[-2] = int(input_str[-1] != "0")

    for index in range(length - 2, -1, -1):
        cur_val = input_str[index]
        next_val = input_str[index + 1]

        if (cur_val == "0" or int(cur_val) > 2) and next_val == "0":
            return 0

        dp[index] = get_cur_val(cur_val, next_val, dp, index)

    return dp[0]
