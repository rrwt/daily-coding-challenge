"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example,
    if A is abcde and B is cdeab, return true.
    If A is abc and B is acb, return false.
"""


def can_shift_a_to_get_b(a: str, b: str) -> bool:
    """
    O(n*n) & O(1)
    """
    len_a = len(a)
    len_b = len(b)

    if len_a != len_b:
        return False

    start_index = 0

    while start_index < len_a:
        if a[start_index] == b[0] and a[start_index:] + a[:start_index] == b:
            return True
        start_index += 1

    return False


if __name__ == "__main__":
    assert can_shift_a_to_get_b("abcde", "cdeab") is True
    assert can_shift_a_to_get_b("abc", "acb") is False
    assert can_shift_a_to_get_b("abc", "ab") is False
