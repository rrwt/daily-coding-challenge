"""
Convert Postfix to Infix Expression
Example:
    Input: Postfix expression:  A B +
    Output: Infix expression- (A + B)

    Input: Postfix expression:  ABC/-AK/L-*
    Output: Infix expression: ((A-(B/C))*((A/K)-L))
"""
from typing import List


operators = ("+", "-", "*", "/")


def convert(postfix: List[str]) -> str:
    stack = []

    while postfix:
        char = postfix.pop()
        if char in operators or stack[-1] in operators:
            stack.append(char)
        else:
            while stack and stack[-1] not in operators:
                op2 = stack.pop()
                operator = stack.pop()
                char = f"({char}{operator}{op2})"
            stack.append(char)

    return stack[0]


if __name__ == "__main__":
    assert convert(["A", "B", "+"]) == "(A+B)"
    assert (
        convert(["A", "B", "C", "/", "-", "A", "K", "/", "L", "-", "*",])
        == "((A-(B/C))*((A/K)-L))"
    )
