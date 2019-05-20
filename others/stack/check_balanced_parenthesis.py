"""
Given an expression string exp , write a program to examine whether
the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print true for exp = “[()]{}{[()()]()}”
and false for exp = “[(])”
"""
matching = {"{": "}", "(": ")", "[": "]"}
openings = set(("(", "[", "{"))
closings = set((")", "]", "}"))


def is_balanced(expression: str) -> bool:
    stack: list = []

    for c in expression:
        if c in openings:
            stack.append(c)
        elif c in closings:
            if not stack or c != matching.get(stack.pop()):
                return False
        else:
            return False

    return False if stack else True


if __name__ == "__main__":
    print(is_balanced("[()]{}{[()()]()}"))
    print(is_balanced("[(])"))
