"""Max profit with atmost k transactions
Given the prices of stock for n days, where you buy and sell.
Get max profit if you are allowed to havee atmost k transactions.
"""


def max_profit(prices: int, k: int) -> int:
    """
    The max profit given a maximum of k transactions would be the maximum of
        1. The max profit of previous day (Not transacting at all on the given day)
        2. jth day profit from previous days + 1 more transaction from j to current.
    
    A matrix (k rows and n columns) can be created for this.
    Matrix[i][j] = max(
        Matrix[i][j-1],  # excluding current
        max(Matrix[i-1][m]+price[j]-price[m])  # including current
    )
        where, i = ith transaction (0..k)
               j = jth day (0..len(arr))
               m ∑ 0..j
    Time Complexity: O(days*days*k)
    Space Complexity: O(days*k)
    """

    def including_current(mat: list, row: int, col: int) -> int:
        res: int = 0

        for m in range(col):
            res = max(res, mat[row - 1][m] + prices[col] - prices[m])

        return res

    num_days: int = len(prices)
    matrix: list = [[0] * num_days for _ in range(k + 1)]

    for transaction in range(1, k + 1):
        for day in range(num_days):
            matrix[transaction][day] = max(
                matrix[transaction][day - 1],
                including_current(matrix, transaction, day),
            )

    return matrix[k][num_days - 1]


def max_profit_fast(prices: int, k: int) -> int:
    """
    Optimizing the second part of above solution. We do not need to calculate the max include
    current everytime. Maxdiff can be used
    Time Complexity: O(days*k)
    Space Complexity: O(days*k)
    """
    num_days: int = len(prices)
    matrix: list = [[0] * num_days for _ in range(k + 1)]

    for trans in range(1, k + 1):
        maxdiff: int = -prices[0]

        for day in range(1, num_days):
            matrix[trans][day] = max(matrix[trans][day - 1], prices[day] + maxdiff)
            maxdiff = max(matrix[trans - 1][day] - prices[day], maxdiff)

    return matrix[k][num_days - 1]


if __name__ == "__main__":
    arr_list: list = [
        [10, 22, 5, 75, 65, 80],
        [2, 30, 15, 10, 8, 25, 80],
        [100, 30, 15, 10, 8, 25, 80],
        [90, 80, 70, 60, 50],
        [2, 5, 7, 1, 4, 3, 1, 3],
    ]
    k_list: int = [2, 2, 2, 2, 3]
    sol_list: list = [87, 100, 72, 0, 10]

    for arr, k, sol in zip(arr_list, k_list, sol_list):
        assert max_profit(arr, k) == sol
        assert max_profit_fast(arr, k) == sol
