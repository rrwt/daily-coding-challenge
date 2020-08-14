"""
Given a number represented by a list of digits, find the next greater permutation of a number,
in terms of lexicographic ordering. If there is not greater permutation possible,
return the permutation with the lowest value/ordering.

For example,
    The list [1,2,3] should return [1,3,2].
    The list [1,3,2] should return [2,1,3].
    The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""
from typing import List


def next_greatest_perm(number: List[int]) -> List[int]:
    """
    1. Find the index of first number from right,
        which is smaller than the number immediately to it's right.
    2. Swap it with the smallest number greater than it and to it's right.
    3. Sort the list from index + 1 to end.
    """
    length = len(number)
    if length < 2:
        return number

    while True:
        f_index = length - 2

        while f_index > -1:
            if number[f_index] < number[f_index + 1]:
                s_index = f_index + 1
                smallest = number[s_index]

                for j in range(f_index + 2, length):
                    if number[f_index] < number[j] < smallest:
                        s_index = j

                number[f_index], number[s_index] = number[s_index], number[f_index]
                number = number[: f_index + 1] + sorted(number[f_index + 1 :])
                break
            f_index -= 1
        else:  # at highest value
            number.sort()

        yield number


if __name__ == "__main__":
    original = [1, 2, 3]
    print("permutations for: ", original)
    gen = next_greatest_perm(original[::])

    while (res := next(gen)) != original:
        print(res)

    original = [1, 2, 5, 6, 7]
    print("permutations for: ", original)
    gen = next_greatest_perm(original[::])

    while (res := next(gen)) != original:
        print(res)
