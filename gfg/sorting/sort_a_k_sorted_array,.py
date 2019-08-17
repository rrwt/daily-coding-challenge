"""
Given an array of n elements, where each element is at most k away from its target position,
devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2,
an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
"""
import heapq
import copy


def min_heap(arr: list, k: int) -> list:
    """
    Create a min heap of k+1 elements (using first k+1 elements), pop and push one by one
    Time Complexity: O(k+(n-k)log(k))
    Space Complexity: O(k)
    """
    l: int = len(arr)
    heap = copy.copy(arr[: k + 1])
    heapq.heapify(heap)

    for i in range(k + 1, l):
        arr[i - k - 1] = heapq.heappushpop(heap, arr[i])

    for i in range(l - k - 1, l):
        arr[i] = heapq.heappop(heap)

    return arr


if __name__ == "__main__":
    arr_list: list = [[6, 5, 3, 2, 8, 10, 9], [10, 9, 8, 7, 4, 70, 60, 50]]
    k_list: list = [3, 4]

    for arr, k in zip(arr_list, k_list):
        print(min_heap(arr, k))
