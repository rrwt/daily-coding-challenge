"""
Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression
and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray",
your function should return true. The same regular expression on the string
"raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return false.
"""
from typing import Tuple


def match(string: str, ind_str: int, len_str: int, regex: str, ind_reg: int, len_reg: int) -> bool:
    """
    Match everything but asterisk
    """
    if ind_reg >= len_reg:
        return ind_str >= len_str
    if ind_str >= len_str:
        return regex[ind_reg:] == "*"
    if string[ind_str] == regex[ind_reg] or regex[ind_reg] == ".":
        return True

    return False


def match_asterisk(
        string: str, ind_str: int, len_str: int, regex: str, ind_reg: int, len_reg: int
) -> Tuple[int, int]:
    """
    Match asterisk. Try to gobble everything.
    """
    while ind_str < len_str and (string[ind_str] == regex[ind_reg-1] or regex[ind_reg-1] == "."):
        ind_str += 1

        if len_str - ind_str == len_reg - ind_reg - 1:
            break

    return ind_str, ind_reg + 1


def regex_match(input_string: str, regex: str) -> bool:
    def util(ind_str: int, ind_reg: int) -> bool:
        nonlocal len_str, len_reg

        # while both present and equal (.)
        while match(input_string, ind_str, len_str, regex, ind_reg, len_reg):
            if ind_reg >= len_reg or ind_str >= len_str:
                break

            ind_str += 1
            ind_reg += 1

        if ind_reg < len_reg and regex[ind_reg] == "*":
            # while match
            return util(*match_asterisk(input_string, ind_str, len_str, regex, ind_reg, len_reg))

        if ind_str >= len_str and ind_reg >= len_reg:
            return True

        return False

    len_str = len(input_string)
    len_reg = len(regex)
    return util(0, 0)


if __name__ == "__main__":
    assert regex_match("ray", "ra.") is True
    assert regex_match("raymond", "ra.") is False
    assert regex_match("chat", ".*at") is True
    assert regex_match("chats", ".*at") is False
