"""
Given an infix expression, convert it into a postfix one and vice-versa
e.g. a+b*c+d => abc*+d+
e.g. abc*+d+ => ((a+(b*c))+d)
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
    """
    read from left to right
    1. operand -> store in output
    2. for operator
        i. if empty stack or operand precedence > stack's top operand precedence, then push
        ii. otherwise pop and append to result until previous condition is met
    3. for (: push to stack
    4. for ): pop and add to output until ( occurs
    5. repeat
    """
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


def postfix_to_infix(postfix: str) -> str:
    """
    start reading from beginning
    1. every operand gets pushed into the stack
    2. for every operator, pop 2 operands and push (op1 op op2) back into stack
    3. repeat
    """
    stack: list = []

    for c in postfix:
        if c.isalpha():
            stack.append(c)
        else:
            op2: str = stack.pop()
            op1: str = stack.pop()
            stack.append(f"({op1}{c}{op2})")

    return stack[0]


if __name__ == "__main__":
    assert infix_to_postfix("a+b*c+d") == "abc*+d+"
    assert infix_to_postfix("A*(B+C*D)+E") == "ABCD*+*E+"
    assert infix_to_postfix("(A+B)*(C-D)") == "AB+CD-*"
    assert postfix_to_infix("abc*+d+") == "((a+(b*c))+d)"
