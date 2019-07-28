"""
Given two equally sized arrays (A, B) and N (size of both arrays).
A sum combination is made by adding one element from array A and another element of array B.
Display the maximum K valid sum combinations from all the possible sum combinations.
Examples:
Input :  A[] : {3, 2},  B[] : {1, 4}, K : 2
Output : 7    // (A : 3) + (B : 4)
         6    // (A : 2) + (B : 4)
Input :  A[] : {4, 2, 5, 1}, B[] : {8, 0, 3, 5}, K : 3
Output : 13   // (A : 5) + (B : 8)
         12   // (A : 4) + (B :  8)
         10   // (A : 2) + (B : 8)  
"""
import heapq


def k_max_sum(a: list, b: list, n: int, k: int) -> list:
    """
    Using min heap of largest k elements
    Time Complexity: O(n*n*log(k))
    Space Complexity: O(n)
    """

    min_heap: list = []
    result: list = [None] * k
    heapq.heapify(min_heap)

    for i in range(n):
        for j in range(n):
            el: int = a[i] + b[j]
            if len(min_heap) < k:
                heapq.heappush(min_heap, el)
            else:
                if el > min_heap[0]:
                    heapq.heappushpop(min_heap, el)

    for i in range(k - 1, -1, -1):
        result[i] = heapq.heappop(min_heap)

    return result


if __name__ == "__main__":
    a: list = [[3, 2], [4, 2, 5, 1], [-10, 14, 11, -5, 12]]
    b: list = [[1, 4], [8, 0, 3, 5], [16, -10, -3, 13, 11]]
    length: list = [2, 4, 5]
    k_list: list = [2, 3, 5]
    res: list = [[7, 6], [13, 12, 10], [30, 28, 27, 27, 25]]

    for x, y, r, l, k in zip(a, b, res, length, k_list):
        assert k_max_sum(x, y, l, k) == r

