"""
Given a string, return the first recurring character in it,
or null if there is no recurring character.

For example,
    given the string "acbbac", return "b". Given the string "abcdef", return null.
"""
from typing import Optional


def first_recurring(text: str) -> Optional[str]:
    prev_char = set()

    for char in text:
        if char in prev_char:
            return char
        else:
            prev_char.add(char)

    return None


if __name__ == "__main__":
    assert first_recurring("acbbac") == "b"
