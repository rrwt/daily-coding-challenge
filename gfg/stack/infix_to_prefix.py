"""
Given a Prefix expression, convert it into a Infix expression and vice-versa
"""
from gfg.stack.infix_to_postfix import infix_to_postfix  # type: ignore


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


def infix_to_prefix(infix: str) -> str:
    """
    reverse the input including ( -> ) and ) -> (
    apply prefix to postfix
    reverse the output and return
    """
    new_infix: list = list(infix[::-1])

    for i, c in enumerate(new_infix):
        if c == "(":
            new_infix[i] = ")"
        elif c == ")":
            new_infix[i] = "("

    res: str = infix_to_postfix("".join(new_infix))
    return res[::-1]


if __name__ == "__main__":
    print(infix_to_prefix("A+(B*C)+D"))
    print(prefix_to_infix("*+AB-CD"))
    print(infix_to_prefix("((A+B)*(C-D))"))
    assert infix_to_prefix(prefix_to_infix("*+AB-CD")) == "*+AB-CD"
    assert infix_to_prefix(prefix_to_infix("*-A/BC-/AKL")) == "*-A/BC-/AKL"
