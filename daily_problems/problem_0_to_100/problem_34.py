"""
Given a string, find the palindrome that can be made by inserting the fewest
number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".
"""


def lexicographic_palindrome(text: str, start: int = -1, end: int = -1) -> str:
    if not text:
        return ""
    if start == -1 and end == -1:
        start, end = 0, len(text) - 1

    if end < start:
        return ""

    if start == end:
        return text[start]

    if text[start] == text[end]:
        return text[start] + lexicographic_palindrome(text, start+1, end-1) + text[end]

    res_1 = text[start] + lexicographic_palindrome(text, start + 1, end) + text[start]
    res_2 = text[end] + lexicographic_palindrome(text, start, end - 1) + text[end]

    if len(res_1) == len(res_2):
        return res_1 if text[start] < text[end] else res_2
    return res_1 if len(res_1) < len(res_2) else res_2


def find_min_insertions_palindrome(text: str) -> int:
    """
    To just find the number of insertions. Not actual palindrome
    """
    length = len(text)

    if length < 2:
        return 0

    dp = [[0] * length for _ in range(length)]

    for gap in range(1, length):
        left = 0

        for right in range(gap, length):
            if text[left] == text[right]:
                dp[left][right] = dp[left + 1][right - 1]
            else:
                dp[left][right] = 1 + min(dp[left + 1][right], dp[left][right - 1])

            left += 1

    return dp[0][length - 1]


if __name__ == "__main__":
    assert lexicographic_palindrome("") == ""
    assert lexicographic_palindrome("a") == "a"
    assert lexicographic_palindrome("ab") == "aba"
    assert lexicographic_palindrome("race") == "ecarace"
    assert lexicographic_palindrome("google") == "elgoogle"

    assert find_min_insertions_palindrome("") == 0
    assert find_min_insertions_palindrome("a") == 0
    assert find_min_insertions_palindrome("ab") == 1
    assert find_min_insertions_palindrome("race") == 3
    assert find_min_insertions_palindrome("google") == 2
