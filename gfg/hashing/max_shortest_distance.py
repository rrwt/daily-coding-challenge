"""
Pair with given sum and maximum shortest distance from end
Given an array of N integers and an integer K,
pick two distinct elements whose sum is K and
find the maximum shortest distance of the picked elements from the endpoints.
e.g.
Input : a[] = {2, 4, 3, 2, 1}
        k = 5.
Output :  2
Explanation:
Select the pair(4, 1). 
Shortest distance of 4 from ends = 2
Shortest distance of 1 from ends = 1
Hence, answer is max(2, 1) = 2   
"""


def max_shortest_dist(arr: list, k: int) -> int:
    d: dict = {}
    l = len(arr)

    for i, e in enumerate(arr):
        if e in d:
            d[e] = min(d[e], i + 1)
        else:
            d[e] = min(i, l - i)

    min_max = 10 ** 10

    for e in arr:
        if k - e in d:
            min_max = min(min_max, max(d[e], d[k - e]))

    return min_max


if __name__ == "__main__":
    print(max_shortest_dist([3, 5, 8, 6, 7], 11))
