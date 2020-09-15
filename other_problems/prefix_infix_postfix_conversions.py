"""
Objective: Given a Prefix expression, write an algorithm to convert it into Infix expression.

Example:
    Input: Prefix expression:  + A B
    Output: Infix expression- (A + B)

    Input: Prefix expression:  *-A/BC-/AKL
    Output: Infix expression: ((A-(B/C))*((A/K)-L))
"""

operators = ("-", "+", "*", "/")


def prefix_to_infix(prefix: str) -> str:
    stack = []

    for index in range(len(prefix) - 1, -1, -1):
        val = prefix[index]

        if val not in operators:
            stack.append(val)
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(f"({operand_1}{val}{operand_2})")

    return stack[0]


def postfix_to_infix(postfix: str) -> str:
    stack = []

    for index in range(len(postfix)):
        val = postfix[index]
        if val not in operators:
            stack.append(val)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.append(f"({operand_1}{val}{operand_2})")

    return stack[0]


def postfix_to_prefix(postfix: str) -> str:
    stack = []

    for index in range(len(postfix)):
        val = postfix[index]
        if val not in operators:
            stack.append(val)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            stack.append(f"{val}{operand_1}{operand_2}")

    return stack[0]


def prefix_to_postfix(prefix: str) -> str:
    stack = []

    for index in range(len(prefix) -1, -1, -1):
        val = prefix[index]

        if val not in operators:
            stack.append(val)
        else:
            operand_1 = stack.pop()
            operand_2 = stack.pop()
            stack.append(f"{operand_1}{operand_2}{val}")

    return stack[0]


if __name__ == "__main__":
    print("prefix to infix")
    print("+AB ->", prefix_to_infix("+AB"))
    print("*-A/BC-/AKL ->", prefix_to_infix("*-A/BC-/AKL"))

    print("prefix to postfix")
    print("+AB ->", prefix_to_postfix("+AB"))
    print("*-A/BC-/AKL ->", prefix_to_postfix("*-A/BC-/AKL"))

    print("postfix to infix")
    print("ABC++ ->", postfix_to_infix("ABC++"))
    print("AB*C+ ->", postfix_to_infix("AB*C+"))
    print("XY*AZ*/B+ ->", postfix_to_infix("XY*AZ*/B+"))
    print("ABC/-AK/L-* ->", postfix_to_infix("ABC/-AK/L-*"))

    print("postfix to prefix")
    print("ABC++ ->", postfix_to_prefix("ABC++"))
    print("AB*C+ ->", postfix_to_prefix("AB*C+"))
    print("XY*AZ*/B+ ->", postfix_to_prefix("XY*AZ*/B+"))
    print("ABC/-AK/L-* ->", postfix_to_prefix("ABC/-AK/L-*"))
