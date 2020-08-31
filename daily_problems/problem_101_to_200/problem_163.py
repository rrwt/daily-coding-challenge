"""
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.
The expression is given as a list of numbers and operands.

For example: [5, 3, '+'] should return 5 + 3 = 8.
For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5,
             since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""
from operator import add, sub, mul, truediv

precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
operators = {"+": add, "-": sub, "*": mul, "/": truediv}


def reverse_polish(notation: list) -> float:
    stack = [notation.pop()]

    while notation:
        cur = notation.pop()
        if cur in operators or stack[-1] in operators:
            stack.append(cur)
        else:
            b = stack.pop()
            oper = stack.pop()
            stack.append(operators[oper](cur, b))

    while len(stack) > 2:
        a = stack.pop()
        b = stack.pop()
        oper = stack.pop()
        stack.append(operators[oper](a, b))

    return stack[0]


if __name__ == "__main__":
    assert reverse_polish([5, 3, "+"]) == 8
    assert reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5
