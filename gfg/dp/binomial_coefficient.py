"""
Write a function that takes two parameters n and k
and returns the value of Binomial Coefficient C(n, k).
For example,
    your function should return 6 for n = 4 and k = 2,
    and it should return 10 for n = 5 and k = 2.
"""


def bin_coef_dp(n: int, k: int) -> int:
    """
    Formula: C(n, k) = C(n-1, k-1) + C(n-1, k)
    Time Complexity: O(n*k)
    Space Complexity: O(n*k)
    """
    c = [[0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        c[i][0] = 1

        for j in range(1, 1 + min(i, k)):
            c[i][j] = c[i-1][j-1] + c[i-1][j]

    return c[n][k]


def bin_coef_efficient(n: int, k: int) -> int:
    """
    C(n, k) = C(n, n-k)  # fact
    therefore, if k > n-k, change k for n-k (for easier calculation)
    i.e. C(n, k) = n! / (k! * (n-k)!) = [(n) * (n-1) * ... (n-k+1) / k!]
     => k terms above and k terms below

    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    if k > n-k:
        k = n-k

    res = 1

    for i in range(k):
        res = res * (n-i) / (k-i)

    return int(res)


if __name__ == "__main__":
    for pair in ((4, 2), (5, 2)):
        print(bin_coef_dp(*pair))
        print(bin_coef_efficient(*pair))
