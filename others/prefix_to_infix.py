"""
Given a Prefix expression, convert it into a Infix expression.
"""


def prefix_to_infix(prefix: str) -> str:
    """
    iterate over prefix expression in reverse
    1. if operands: push to stack
    2. if operator: pop 2 operands from stack and create: (op1 op op2)
    3. push result back to stack
    4. repeat
    """
    stack: list = []

    for c in reversed(prefix):
        if c.isalpha():
            stack.append(c)
        else:
            expr: str = f"({stack.pop()}{c}{stack.pop()})"
            stack.append(expr)

    return stack[0]


if __name__ == "__main__":
    print(prefix_to_infix("*+AB-CD"))
    print(prefix_to_infix("*-A/BC-/AKL"))
