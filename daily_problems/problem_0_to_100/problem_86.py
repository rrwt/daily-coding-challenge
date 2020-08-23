"""
Given a string of parentheses, write a function to compute the minimum number of parentheses
to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example,
    given the string "()())()", you should return 1.
    Given the string ")(", you should return 2, since we must remove all of them.
"""


def count_remove_parenthesis(text: str) -> int:
    count_removal = 0
    stack = []

    for char in text:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] == ")":
                count_removal += 1
            else:
                stack.pop()
        else:
            raise AssertionError(f"{char} is unacceptable as a parenthesis")

    return count_removal + len(stack)


if __name__ == "__main__":
    assert count_remove_parenthesis("()())()") == 1
    assert count_remove_parenthesis(")(") == 2
    assert count_remove_parenthesis("") == 0
    assert count_remove_parenthesis("((()))") == 0
    assert count_remove_parenthesis("()(") == 1
    assert count_remove_parenthesis("((()())())()()()(())") == 0
