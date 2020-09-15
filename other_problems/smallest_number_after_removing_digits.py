"""
Given a number with N digits, write a program to get the
smallest number possible after removing k digits from number N.
"""


def get_smallest(num: int, k: int) -> int:
    num_lst = [int(n) for n in list(str(num))]
    stack = []
    index = 0
    size = len(num_lst)

    while index < size and k > 0:
        if not stack or stack[-1] <= num_lst[index]:
            stack.append(num_lst[index])
            index += 1
        else:
            stack.pop()
            k -= 1

    if index < size:
        stack.extend(num_lst[index:])
    elif k > 0:
        stack = stack[:-k]

    return int("".join([str(n) for n in stack]))


if __name__ == "__main__":
    assert get_smallest(1453287, 3) == 1287
    assert get_smallest(4321, 2) == 21
    assert get_smallest(22222, 3) == 22
    assert get_smallest(2200010300, 4) == 0
    assert get_smallest(4205123, 4) == 12
