"""
Given an array of integers. Write a program to find the K-th largest sum of
contiguous subarray within the array of numbers which has negative and positive numbers.
Input: a[] = {20, -5, -1}, k = 3
Output: 14
Explanation: All sum of contiguous subarrays are (20, 15, 14, -5, -6, -1)
so the 3rd largest sum is 14.

Input: a[] = {10, -10, 20, -40}, k = 6
Output: -10
Explanation: The 6th largest sum among sum of all contiguous subarrays is -10.
"""
import heapq
from typing import Tuple


def largest_sum(arr: list, k: int) -> Tuple[list, int]:
    """
    Sum of elements from i to j can be calculated as sum[0:j]-sum[0:i-1]
    We can store first k sums in a min heap and replace as required.
    After processing all of the elements, the root of min heap will be the solution,
    and the min heap will have the k largest elements.
    Time Complexity: O(n*nlog(k))
    Space Complexity: O(n)
    """
    l: int = len(arr)
    sum_arr: list = [0]  # for sum_arr[i-1], when i is 0

    for i in range(1, l + 1):
        sum_arr.append(sum_arr[i - 1] + arr[i - 1])

    min_heap: list = []

    for i in range(1, l + 1):
        for j in range(i, l + 1):
            temp_sum = sum_arr[j] - sum_arr[i - 1]

            if len(min_heap) < k:
                heapq.heappush(min_heap, temp_sum)
            elif temp_sum > min_heap[0]:
                heapq.heapreplace(min_heap, temp_sum)

    return min_heap, min_heap[0]


if __name__ == "__main__":
    print(largest_sum([20, -5, -1], 3))
    print(largest_sum([10, -10, 20, -40], 6))
