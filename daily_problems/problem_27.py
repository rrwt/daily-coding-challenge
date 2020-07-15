"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
"""

OPENING = {"(", "[", "{"}
OPEN_CLOSE = {"(": ")", "[": "]", "{": "}"}


def balanced_paranthesis(paranthesis: str) -> bool:
    """
    A stack can be used to keep the unbalanced paranthesis while matching paranthesis has not
    been found
    """
    stack: list = []

    for p in paranthesis:
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
    assert balanced_paranthesis(p1) == True
    assert balanced_paranthesis(p2) == False
    assert balanced_paranthesis(p3) == False
