"""
Given an array of integers where each element represents the max number of
steps that can be made forward from that element. Write a function to return
the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.
"""
import sys
from typing import Tuple


def print_jump(jump_list: list) -> None:
    print(*jump_list, sep="->")


def min_jumps(arr: list, index: int, length: int) -> Tuple[int, list]:
    """Recursive
    Time Complexity: O(n*n!)
    Space Complexity: O(n)
    """
    if index == length - 1:
        return 0, [length - 1]
    elif index >= length:
        return sys.maxsize, []
    else:
        jumps: int = sys.maxsize
        jump_list: list = []

        for i in range(index + 1, min(arr[index] + index + 1, length)):
            curr_jumps, j_list = min_jumps(arr, i, length)

            if curr_jumps < jumps:
                jump_list = j_list
                jumps = curr_jumps

        if index == 0:
            print(jump_list)

        return jumps + 1, [index] + jump_list


def min_jumps_dp(arr: list) -> int:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(n)
    """

    def solution(index: int):
        nonlocal jump_arr, length
        if jump_arr[index] == sys.maxsize:
            for i in range(index + 1, min(arr[index] + index + 1, length)):
                jump_arr[index] = min(jump_arr[index], 1 + solution(i))

        return jump_arr[index]

    length: int = len(arr)
    jump_arr: list = [sys.maxsize] * length
    jump_arr[length - 1] = 0

    solution(0)
    return jump_arr[0]


def min_jumps_linear(arr: list) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    length: int = len(arr)
    max_reach, jumps, steps = arr[0], 0, arr[0]

    for index in range(1, length):
        if index == length - 1:
            return jumps + 1

        max_reach = max(max_reach, index + arr[index])
        steps -= 1

        if steps == 0:
            # index + steps = reach in 1 jump.
            # No need to increment jump for that many steps
            jumps += 1
            steps = max_reach - index

    return -1


if __name__ == "__main__":
    arr_list: list = [[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]]
    res_list: list = [3]

    for arr, res in zip(arr_list, res_list):
        assert min_jumps(arr, 0, len(arr))[0] == res
        assert min_jumps_dp(arr) == res
        assert min_jumps_linear(arr) == res
