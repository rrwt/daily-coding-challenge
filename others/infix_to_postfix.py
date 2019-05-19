"""
Given an infix expression, convert it into a postfix one
e.g. a+b*c+d => abc*+d+
"""


def precedence(operator: str) -> int:
    if operator == "^":
        return 3
    elif operator in ("*", "/"):
        return 2
    elif operator in ("+", "-"):
        return 1
    return 0


def infix_to_postfix(infix: str) -> str:
    result: str = ""
    stack: list = []

    for c in infix:
        if c.isalpha():
            result += c
        else:
            if c == ")":
                op: str = stack.pop()

                while op != "(":
                    result += op
                    op = stack.pop()
            elif c == "(":
                stack.append(c)
            else:
                while stack and precedence(c) <= precedence(stack[-1]):
                    result += stack.pop()
                stack.append(c)

    while stack:
        result += stack.pop()

    return result


if __name__ == "__main__":
    assert infix_to_postfix("a+b*c+d") == "abc*+d+"
    assert infix_to_postfix("A*(B+C*D)+E") == "ABCD*+*E+"
    assert infix_to_postfix("(A+B)*(C-D)") == "AB+CD-*"
