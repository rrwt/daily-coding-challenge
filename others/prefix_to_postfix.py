"""
Convert from prefix to postfix and vice-versa

Easiest solution would be to traverse through infix. Better solution is direct conversion
"""


def prefix_to_postfix(prefix: str) -> str:
    stack: list = []

    for c in prefix[::-1]:
        if c.isalpha():
            stack.append(c)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"{op1}{op2}{c}")

    return stack[0]


def postfix_to_prefix(postfix: str) -> str:
    stack: list = []

    for c in postfix:
        if c.isalpha():
            stack.append(c)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"{c}{op1}{op2}")

    return stack[0]


if __name__ == "__main__":
    assert prefix_to_postfix("*+AB-CD") == "AB+CD-*"
    assert prefix_to_postfix("*-A/BC-/AKL") == "ABC/-AK/L-*"
    assert postfix_to_prefix("AB+CD-*") == "*+AB-CD"
    assert postfix_to_prefix("ABC/-AK/L-*") == "*-A/BC-/AKL"
