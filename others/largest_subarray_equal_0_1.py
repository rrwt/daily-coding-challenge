"""
Given an array containing only 0s and 1s, find the largest subarray which
contain equal no of 0s and 1s. Expected time complexity is O(n). 
"""
from array import array


def largest_subarray(arr):
    sum_arr = array('b', [1 if arr[0] == 1 else -1])
    max_len = 0
    d = {}
    end_index = -1

    for i, a in enumerate(arr[1:]):
        sum_arr.append(sum_arr[i] + (1 if a == 1 else -1))

        if sum_arr == 0:
            max_len = i+1
            end_index = i

    for i, v in enumerate(sum_arr):
        if v in d:
            if i-d[v] > max_len:
                max_len = i-d[v]
                end_index = i
        else:
            d[v] = i

    print(end_index-max_len+1, end_index)
    return max_len


if __name__ == "__main__":
    print(largest_subarray([1, 0, 1, 1, 1, 0, 0]) == 6)
