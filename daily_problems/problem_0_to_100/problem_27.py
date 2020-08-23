"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

OPENING = {"(", "[", "{"}
OPEN_CLOSE = {"(": ")", "[": "]", "{": "}"}


def balanced_parenthesis(parenthesis: str) -> bool:
    """
    A stack can be used to keep the unbalanced parenthesis
    while matching parenthesis has not been found
    """
    stack: list = []

    for p in parenthesis:
        if p in OPENING:
            stack.append(p)
        elif not stack:
            return False
        else:
            q = stack.pop()

            if q not in OPENING or OPEN_CLOSE[q] != p:
                return False

    return False if stack else True


if __name__ == "__main__":
    p1: str = "([])[]({})"
    p2: str = "([)]"
    p3: str = "((()"
    assert balanced_parenthesis(p1) is True
    assert balanced_parenthesis(p2) is False
    assert balanced_parenthesis(p3) is False
