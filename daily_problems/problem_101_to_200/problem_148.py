"""
Gray code is a binary code where each successive value differ in only one bit,
as well as when wrapping around. Gray code is common in hardware so that we
don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.
For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def _flip_bit(bit: str) -> str:
    return "0" if bit == "1" else "1"


def _generator(n: int, prev_val: str, values: set) -> list:
    for _ in range(n - 1, -1, -1):
        new_val = prev_val[:_] + _flip_bit(prev_val[_]) + prev_val[_ + 1 :]

        if new_val not in values:
            values.add(new_val)
            return [new_val] + _generator(n, new_val, values)

    return []


def gray_codes(n: int) -> list:
    first_val = "0" * n
    return [first_val] + list(_generator(n, first_val, {first_val}))


if __name__ == "__main__":
    for _ in range(5):
        print(gray_codes(_))
