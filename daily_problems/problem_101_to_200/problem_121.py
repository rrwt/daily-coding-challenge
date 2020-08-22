"""
Given a string which we can delete at most k, return whether you can make a palindrome.
For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""


def _make_palindrome(text: str, start: int, end: int, k: int) -> bool:
    if end - start <= k:
        return True

    if k < 0:
        return False

    is_pal = False

    if text[start] == text[end]:
        if end in (start, start + 1):
            return True

        is_pal = _make_palindrome(text, start + 1, end - 1, k)

    return (
        is_pal
        or _make_palindrome(text, start + 1, end, k - 1)
        or _make_palindrome(text, start, end - 1, k - 1)
    )


def make_palindrome_naive(text: str, k: int) -> bool:
    """
    Time Complexity: O(2^n)
    """
    return _make_palindrome(text, 0, len(text) - 1, k)


def make_palindrome_dp(text: str, k: int) -> bool:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(n*n)
    """
    str_len = len(text)
    dp = [[0] * str_len for _ in range(str_len)]

    for length in range(2, str_len + 1):
        for start in range(0, str_len - length + 1):
            end = start + length - 1

            if length == 2:
                dp[start][end] = 0 if text[start] == text[end] else 1
            elif text[start] == text[end]:
                dp[start][end] = dp[start + 1][end - 1]
            else:
                dp[start][end] = min(dp[start + 1][end], dp[start][end - 1]) + 1

    return dp[0][-1] <= k


if __name__ == "__main__":
    assert make_palindrome_naive("waterrfetawx", 2) is True
    assert make_palindrome_dp("waterrfetawx", 2) is True
