"""
Given a string, return whether it represents a number. Here are the different kinds of numbers:
    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

And here are examples of non-numbers:
    "a"
    "x 1"
    "a -2"
    "-"
"""


def verify_beginning(text: str) -> bool:
    return text[0] in ("-", "+") or text[0].isdigit()


def verify_body(text: str) -> bool:
    len_text = len(text)

    if len_text > 2:
        count_e = 0
        count_dot = 0
        count_plus = 0
        count_minus = 0

        for index in range(1, len_text - 1):
            if text[index] == "e":
                if count_e > 0:
                    return False
                count_e += 1
            elif text[index] == ".":
                if count_e > 0 or count_dot > 0:
                    return False
                count_dot += 1
            elif text[index] in ("+", "-"):
                if text[index - 1] != "e" or count_plus > 0 or count_minus > 0:
                    return False
                elif text[index] == "+":
                    count_plus += 1
                else:
                    count_minus += 1
            elif not text[index].isdigit():
                return False

        return count_e < 2 and count_dot < 2
    else:  # No need to test. can be tested with beg and end.
        return True


def verify_end(text: str) -> bool:
    return text[-1].isdigit()


def string_is_number(text: str) -> bool:
    if not text:
        return False

    return verify_beginning(text) and verify_body(text) and verify_end(text)


if __name__ == "__main__":
    assert string_is_number("10.9") is True
    assert string_is_number("-15.7") is True
    assert string_is_number("1") is True
    assert string_is_number("1e5") is True
    assert string_is_number("1.5e+10") is True
    assert string_is_number("5.4e-10") is True
    assert string_is_number("4x3") is False
    assert string_is_number("a") is False
    assert string_is_number("x 1") is False
    assert string_is_number("1 e5") is False
    assert string_is_number("a - 2") is False
    assert string_is_number("10-1") is False
    assert string_is_number("10+1") is False
    assert string_is_number("-") is False
    assert string_is_number("-e") is False
    assert string_is_number("+e") is False
