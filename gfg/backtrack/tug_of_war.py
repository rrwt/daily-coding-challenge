"""
Given a list of n integers, divide the list in two sublists of n/2 sizes each
such that the difference of the sum of two sublists is as minimum as possible.
If n is even, then sizes of two sublists must be strictly n/2 and if n is odd,
then size of one sublist must be (n-1)/2 and size of other sublist must be (n+1)/2.
"""
import sys
from copy import deepcopy


def tow(elements: list) -> tuple:
    s1: list = []
    s2: list = []
    l = len(elements)
    l1, l2 = int((l + 1) / 2), int(l / 2)
    min_diff = sys.maxsize

    def solution(index: int, cur_list1: list, cur_list2: list) -> None:
        nonlocal s1, s2, l, l1, l2, min_diff

        if index == l:
            diff = abs(sum(cur_list1) - sum(cur_list2))
            if diff < min_diff:
                min_diff = diff
                s1 = deepcopy(cur_list1)
                s2 = deepcopy(cur_list2)
        else:
            element = elements[index]
            len_list1 = len(cur_list1)
            len_list2 = len(cur_list2)

            if len_list1 < l1:
                solution(index + 1, cur_list1 + [element], cur_list2)
            if len_list1 == l1:
                solution(l, cur_list1, cur_list2 + elements[index:])
            elif len_list2 < l2:
                solution(index + 1, cur_list1, cur_list2 + [element])

    solution(0, [], [])

    return s1, s2, min_diff


if __name__ == "__main__":
    print(*tow([3, 4, 5, -3, 100, 1, 89, 54, 23, 20]), sep=" and ")
    print(*tow([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]), sep=" and ")
