"""
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example,
    the longest palindromic substring of "aabcdcb" is "bcdcb".
    The longest palindromic substring of "bananas" is "anana".
"""


def longest_palindromic_substring(text: str) -> str:
    """
    Dynamic Programming.
    Time Complexity: O(n*n)
    Space Complexity: O(n*n)
    """
    length = len(text)
    if length < 2:
        return text

    dp = [[1] * length for _ in range(length)]
    max_start, max_end, max_len = 0, 0, 1

    for str_len in range(1, length):
        start = 0

        for end in range(start + str_len, length):
            if text[start] == text[end]:
                if start == end - 1:
                    dp[start][end] = 2
                else:
                    dp[start][end] = dp[start + 1][end - 1] + 2

                if dp[start][end] > max_len:
                    max_len = end - start + 1
                    max_start = start
                    max_end = end

            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

            start += 1

    return text[max_start: max_end + 1]


if __name__ == "__main__":
    assert longest_palindromic_substring("aabcdcb") == "bcdcb"
    assert longest_palindromic_substring("bananas") == "anana"
