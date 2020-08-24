"""
Given an array of numbers representing the stock prices of a company in chronological order
and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""
from typing import List


def max_profit_with_k_buys_and_sells(prices: List[int], max_sells: int) -> int:
    num_prices = len(prices)
    profit = [[0] * num_prices for _ in range(max_sells + 1)]

    for num_sells in range(1, max_sells + 1):  # how many sales are allowed
        for index in range(1, num_prices):  # last selling point
            max_so_far = 0

            # with 1 current sale
            for j in range(index):
                # prev max + 1 sale
                max_so_far = max(
                    max_so_far, prices[index] - prices[j] + profit[num_sells - 1][j],
                )

            # with 1 sale using ith price index vs no transaction using ith price index
            profit[num_sells][index] = max(max_so_far, profit[num_sells][index - 1])

    return profit[max_sells][num_prices - 1]


if __name__ == "__main__":
    assert max_profit_with_k_buys_and_sells([5, 2, 4, 0, 1], 2) == 3
    assert max_profit_with_k_buys_and_sells([10, 22, 5, 75, 65, 80], 2) == 87
