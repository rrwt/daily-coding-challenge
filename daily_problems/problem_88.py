"""
Implement division of two positive integers without using
the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""


def custom_division(numerator: int, denominator: int) -> int:
    """
    Works only if both integers are +ve
    """
    while numerator > denominator:
        numerator -= denominator

    return numerator


def custom_division_all_int(numerator: int, denominator: int) -> int:
    sign_num = numerator > 0
    sign_den = denominator > 0

    sign = -1 if sign_den != sign_num else 1

    result = custom_division(abs(numerator), abs(denominator))
    return -result if sign < 0 else result


if __name__ == "__main__":
    print(custom_division(10, 4))
    print(custom_division_all_int(-10, 3))
