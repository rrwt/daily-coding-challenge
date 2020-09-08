"""
Given a string of parentheses, find the balanced string that can be
produced from it using the minimum number of insertions and deletions.
If there are multiple solutions, return any of them.

For example,
    given "(()", you could return "(())".
    given "))()(", you could return "()()()()".
"""


def get_balanced_parenthesis(parenthesis: str) -> str:
    res = []
    stack = []

    opening = 0
    closing = 0

    for index, value in enumerate(parenthesis):
        if value == "(":
            opening += 1
            stack.append(value)
        elif closing < opening:
            closing += 1
            stack.append(value)

        if closing and closing == opening:
            res.extend(stack)
            stack = []
            opening = closing = 0

    if closing:
        res.extend(stack[opening-closing:])

    return "".join(res)


if __name__ == "__main__":
    print("(() ->", get_balanced_parenthesis("(()"))
    print("))()( ->", get_balanced_parenthesis("))()("))
    print("()(() ->", get_balanced_parenthesis("()(()"))
    print("()(())) ->", get_balanced_parenthesis("()(()))"))
    print(")(()) ->", get_balanced_parenthesis(")(())"))
    print("())( ->", get_balanced_parenthesis("())("))
