"""
Given an array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and
selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
buy the stock at 5 dollars and sell it at 10 dollars.
"""


def max_profit(stocks: list) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    start, end = 0, len(stocks) - 1
    result: int = 0

    while start < end:
        buy = stocks[start]
        index = start + 1
        profit = 0

        while index <= end and buy < stocks[index]:
            profit = max(profit, stocks[index] - buy)
            index += 1

        # because any further investigation would be preferred using this as base
        start = index
        result = max(result, profit)

    return result


if __name__ == "__main__":
    assert max_profit([9, 11, 8, 5, 7, 10]) == 5
