"""
Evaluate an expression represented by a String. Expression can contain
parentheses, you can assume parentheses are well-matched. For simplicity,
you can assume only binary operations allowed are +, -, *, and /
"""
from typing import Union


def precedence(operator: str) -> int:
    if operator in ("/", "*"):
        return 2
    if operator in ("+", "-"):
        return 1
    return 0


def evaluate_expression(expression: str) -> Union[int, float]:
    expre_list: list = expression.split(" ")
    s_num: list = []
    s_oper: list = []

    for e in expre_list:
        if str.isdigit(e):
            s_num.append(e)
        elif e == "(":
            s_oper.append(e)
        elif e == ")":
            temp: str = s_oper.pop()
            while temp != "(":
                op2 = s_num.pop()
                op1 = s_num.pop()
                s_num.append(eval(f"{op1}{temp}{op2}"))
                temp = s_oper.pop()
        else:
            while s_oper and precedence(e) <= precedence(s_oper[-1]):
                op2 = s_num.pop()
                op1 = s_num.pop()
                s_num.append(f"{op1}{s_oper.pop()}{op2}")

            s_oper.append(e)

    while s_oper:
        op2 = s_num.pop()
        op1 = s_num.pop()
        s_num.append(eval(f"{op1}{s_oper.pop()}{op2}"))

    return s_num[0]


if __name__ == "__main__":
    assert evaluate_expression("10 + 2 * 6") == 22
    assert evaluate_expression("100 * 2 + 12") == 212
    assert evaluate_expression("100 * ( 2 + 12 )") == 1400
    assert evaluate_expression("100 * ( 2 + 12 ) / 14") == 100
