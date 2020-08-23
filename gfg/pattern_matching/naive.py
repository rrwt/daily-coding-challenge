"""Brute Force Pattern Matching
"""


def find_substring(string: str, substring: str) -> int:
    """
    Find substring in a larger string.
    """
    i_str: int = 0
    l_str: int = len(string)
    l_sub: int = len(substring)

    while i_str <= l_str - l_sub:
        index = 0

        while index < l_sub and string[index + i_str] == substring[index]:
            index += 1

        if index >= l_sub:
            return i_str
        elif index + i_str >= l_str:
            return -1

        i_str += 1

    return -1


if __name__ == "__main__":
    if (ind := find_substring("THIS IS A TEST TEXT", "TEXT")) > -1:
        print(f"Found at index {ind}")
    else:
        print("Not Found")
