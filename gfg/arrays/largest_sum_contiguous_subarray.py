# Write an efficient program to find the sum of contiguous subarray within
# a one-dimensional array of numbers which has the largest sum.


def max_sum_kadane(nums: list) -> int:
    # kadane's algorithm
    max_so_far = max_ending_here = 0

    for value in nums:
        max_ending_here = max(max_ending_here + value, 0)

        if max_ending_here > 0:
            max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_sum_print_subarray(nums: list) -> int:
    start = s = 0
    end = -1
    max_so_far = max_ending_here = 0

    for index, value in enumerate(nums):
        max_ending_here += value

        if max_ending_here > max_so_far:
            start = s
            end = index
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
            s = index + 1

    return nums[start: end + 1]


if __name__ == "__main__":
    assert max_sum_kadane([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]) == 0
    assert max_sum_print_subarray([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]) == []
    assert max_sum_kadane([-2, -3, 4, -1, -2, 1, 5, -3]) == 7
    assert max_sum_print_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == [4, -1, -2, 1, 5]
