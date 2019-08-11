"""
In a daily share trading, a buyer buys shares in the morning and sells it on same day.
If the trader is allowed to make at most 2 transactions in a day,
where as second transaction can only start after first one is complete (buy->sell->buy->Sell).
Given stock prices throughout day, find out maximum profit that a share trader could have made.
"""


def max_profit_rohit(arr: list) -> int:
    """
    Time Complexity: O(n*n)
    Space Complexity: O(1)
    """

    def transaction(start: int, end: int) -> int:
        """
        Max profit given atmost 1 transaction.
        Time Complexity: O(n)
        """
        if start >= end:
            return 0

        buy_index: int = start
        sell_index: int = start + 1
        max_profit = max(0, arr[sell_index] - arr[buy_index])

        for i in range(start + 1, end + 1):
            if arr[i] < arr[buy_index]:
                buy_index = i
            elif arr[i] > arr[sell_index]:
                sell_index = i
                max_profit = max(max_profit, arr[sell_index] - arr[buy_index])

        return max_profit

    l: int = len(arr)
    j: int = 1
    max_profit: int = 0

    while j < l and arr[j] < arr[j - 1]:
        j += 1

    for i in range(j - 1, l):
        profit = transaction(j - 1, i) + transaction(i + 1, l - 1)
        max_profit = max(max_profit, profit)

    return max_profit


def max_profit_optimized(price_arr: list) -> int:
    """
    1) Create a table profit[0..n-1] and initialize all values in it 0.
    2) Traverse price[] from right to left and update profit[i]
       such that profit[i] stores maximum profit achievable from
       one transaction in subarray price[i..n-1]
    3) Traverse price[] from left to right and update profit[i] such that
       profit[i] stores maximum profit such that profit[i] contains maximum
       achievable profit from two transactions in subarray price[0..i].
    4) Return profit[n-1]

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    arr_len: int = len(price_arr)
    min_price: int = price_arr[0]
    max_price: int = price_arr[arr_len - 1]
    profit_arr: list = [0] * arr_len

    for index in range(arr_len - 2, -1, -1):
        max_price = max(price_arr[index], max_price)
        profit_arr[index] = max(profit_arr[index + 1], max_price - price_arr[index])

    for index in range(1, arr_len):
        min_price = min(price_arr[index], min_price)
        profit_arr[index] = max(
            profit_arr[index - 1], profit_arr[index] + price_arr[index] - min_price
        )

    return profit_arr[arr_len - 1]


if __name__ == "__main__":
    arr_list: list = [
        [10, 22, 5, 75, 65, 80],
        [2, 30, 15, 10, 8, 25, 80],
        [100, 30, 15, 10, 8, 25, 80],
        [90, 80, 70, 60, 50],
    ]
    sol_list: list = [87, 100, 72, 0]

    for arr, sol in zip(arr_list, sol_list):
        assert max_profit_rohit(arr) == sol
        assert max_profit_optimized(arr) == sol
