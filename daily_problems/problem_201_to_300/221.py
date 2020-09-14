"""
Let's define a "seven_ish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few seven_ish numbers are
1, 7, 8, 49, and so on. Create an algorithm to find the nth seven_ish number.
"""


def seven_ish_number(n: int) -> int:
    if n == 1:
        return 1

    nums = [0] * (n + 1)
    nums[1] = 1
    next_power = 1
    last_filled_index = 1

    while last_filled_index < n:
        cur_index = last_filled_index + 1
        power_val = pow(7, next_power)

        for k in range(last_filled_index + 1):
            nums[cur_index] = power_val + nums[k]
            cur_index += 1

            if cur_index > n:
                break

        last_filled_index = cur_index - 1
        next_power += 1

    return nums[n]


if __name__ == "__main__":
    for _ in range(1, 16):
        print(f"{_} -> {seven_ish_number(_)}")
