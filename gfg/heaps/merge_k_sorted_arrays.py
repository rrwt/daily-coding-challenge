"""
Merge K sorted arrays
"""
import heapq
from typing import Sequence, List


def get_next_min(
    array_list: Sequence[List[int]], index_array: List[int], k: int, length: int
) -> int:
    return_value, min_index = 1_000_000, -1

    for i in range(k):
        if index_array[i] < length and array_list[i][index_array[i]] < return_value:
            min_index = i
            return_value = array_list[i][index_array[i]]

    if min_index > -1:
        index_array[min_index] += 1
        return return_value

    raise Exception("Invalid index array")


def merge_arrays(array_list: Sequence[List[int]], k: int, arr_size: int) -> List[int]:
    arr_length = k * arr_size
    return_array = [None] * arr_length
    index: int = 0
    index_arr = [1] * k
    heap = [None] * k

    for i in range(k):
        heap[i] = array_list[i][0]

    heapq.heapify(heap)

    while index < arr_length - k:
        return_array[index] = heapq.heappushpop(
            heap, get_next_min(array_list, index_arr, k, arr_size)
        )
        index += 1

    while index < arr_length:
        return_array[index] = heapq.heappop(heap)
        index += 1

    return return_array


if __name__ == "__main__":
    arr_list: Sequence[List[int]] = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
    print(*merge_arrays(arr_list, 3, 4))
