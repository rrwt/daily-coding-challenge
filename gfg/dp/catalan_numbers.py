# Catalan numbers satisfy the following recursive formula.
# C_0=1 and C_n_+_1=sum(c_i * c_n-i for i in range(n+1))
# there is a binomial coefficient formula: C(n) = 2nC(n) / (n+1)


def catalan_recursive(n: int) -> int:
    # recursive solution for catalan number. Exponential
    if n == 0:
        return 1

    total = 0

    for i in range(n):
        total += catalan_recursive(i) * catalan_recursive(n-i-1)

    return total


def catalan_dp(n: int) -> int:
    # O(n*n)
    catalan = [0] * (n + 1)
    catalan[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]
    
    return catalan[n]


if __name__ == "__main__":
    for num in range(10):
        assert catalan_recursive(num) == catalan_dp(num), f"Assertion failed for {num}"

