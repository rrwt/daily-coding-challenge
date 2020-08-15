"""
Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression
and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray",
your function should return true. The same regular expression on the string
"raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""


def regex_match_naive(text: str, pattern: str) -> bool:
    # recursive solution
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], "."}

    if len(pattern) >= 2 and pattern[1] == "*":
        # 0 match or 1+ match using *
        return regex_match_naive(text, pattern[2:]) or (
            first_match and regex_match_naive(text[1:], pattern)
        )
    else:  # there is no asterisk
        return first_match and regex_match_naive(text[1:], pattern[1:])


def regex_match_dp(text: str, pattern: str) -> bool:
    # dynamic programming solution
    len_t = len(text)
    len_p = len(pattern)
    dp = [[False] * (len_p + 1) for _ in range(len_t + 1)]

    dp[0][0] = True  # both empty

    for index in range(2, len_p + 1):
        if pattern[index - 1] == "*":
            dp[0][index] = dp[0][index - 2]

    for i_t in range(0, len_t):
        for i_p in range(0, len_p):
            if pattern[i_p] == "*" and i_p > 0:
                # 0 occurrence or 1+ occurrence
                # 0 occurrence: res = do not consider * and previous char
                # 1+ occurrences: res = curr text char = previous pattern char and
                # there was a match of current pattern with previous text char
                dp[i_t + 1][i_p + 1] = dp[i_t + 1][i_p - 1] or (
                    pattern[i_p - 1] in (text[i_t], ".") and dp[i_t][i_p + 1]
                )
            else:
                # current text char matches with curr pattern char and
                # there was a match until previous char
                dp[i_t + 1][i_p + 1] = pattern[i_p] in (".", text[i_t]) and dp[i_t][i_p]

    return dp[len_t][len_p]


if __name__ == "__main__":
    assert regex_match_naive("", ".*") is True
    assert regex_match_naive("ray", "ra.") is True
    assert regex_match_naive("raymond", "ra.") is False
    assert regex_match_naive("chat", ".*at") is True
    assert regex_match_naive("chats", ".*at") is False
    assert regex_match_naive("aab", "c*a*b") is True
    assert regex_match_naive("aaa", "ab*ac*a") is True
    assert regex_match_naive("aaa", "ab*a*c*a") is True
    assert regex_match_naive("bbbba", ".*a*a") is True

    # assert regex_match_dp("", ".*") is True
    assert regex_match_dp("ray", "ra.") is True
    assert regex_match_dp("raymond", "ra.") is False
    assert regex_match_dp("chat", ".*at") is True
    assert regex_match_dp("chats", ".*at") is False
    assert regex_match_dp("aab", "c*a*b") is True
    assert regex_match_dp("aaa", "ab*ac*a") is True
    assert regex_match_dp("aaa", "ab*a*c*a") is True
    assert regex_match_dp("bbbba", ".*a*a") is True  # Not working
