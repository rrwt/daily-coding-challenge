"""
Find the maximum sum of continuous subarray in a given array of integers
containing +ve and -ve integers
"""


def continuous_sum(arr):
    max_ = curr_sum = arr[0]
    l = len(arr)

    for i in range(1, l):
        new_sum = max(curr_sum + arr[i], 0)
        curr_sum = max(new_sum, arr[i])

        if curr_sum > max_:
            max_ = curr_sum

    return max(max_, 0)


if __name__ == "__main__":
    print(continuous_sum([-2, 11, -4, 13, -5, -2]))
