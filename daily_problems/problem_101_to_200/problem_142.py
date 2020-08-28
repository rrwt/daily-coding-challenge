"""
You're given a string consisting solely of (, ), and *. * can represent either a (, ),
or an empty string. Determine whether the parentheses are balanced.
For example, (()* and (*) are balanced. )*( is not balanced.
"""


def is_balanced(text: str) -> bool:
    size = len(text)
    index = 0
    stack = []

    while index < size:
        if text[index] == "(":
            stack.append("(")
        elif text[index] == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False

        index += 1

    return not stack


def balanced_parentheses(text: str, index: int = 0) -> bool:
    """
    each * can be one of "", ")", "("
    """
    if not text:
        return True

    if index < len(text):
        if text[index] == "*":
            before = text[:index]
            after = text[index + 1 :]

            return (
                balanced_parentheses(before + after, index)
                or balanced_parentheses(before + ")" + after, index + 1)
                or balanced_parentheses(before + "(" + after, index + 1)
            )
        else:
            return balanced_parentheses(text, index + 1)
    else:
        return is_balanced(text)


if __name__ == "__main__":
    assert balanced_parentheses("(()*") is True
    assert balanced_parentheses("(()*))") is True
    assert balanced_parentheses("(()*)") is True
    assert balanced_parentheses("(*)") is True
    assert balanced_parentheses(")*(") is False
