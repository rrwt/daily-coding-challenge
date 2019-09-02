"""
The stock span problem is a financial problem where we have a series of n daily
price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number
of consecutive days just before the given day, for which the price of the stock on
the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
"""
from array import array


def stock_span(prices: array) -> list:
    """
    Time Complexity: O(n*n)
    """
    span_values: list = []

    for i, price in enumerate(prices):
        count: int = 1

        for j in range(i - 1, -1, -1):
            if prices[j] > price:
                break
            count += 1

        span_values.append(count)

    return span_values


def stock_span_efficient(prices: array) -> list:
    """
    Store index of largest elements so far in stack
    for each array element we can pop stack elements until the stack is not empty
    or the top of stack is greater than the current element.
    the count of popped elements + 1 is the span of that day.
    Time Complexity: O(n)
    """
    stack: list = []
    result: list = []

    for index, value in enumerate(prices):
        while stack and prices[stack[-1]] < value:
            stack.pop()
        if stack:
            result.append(index - stack[-1])
        else:
            result.append(index + 1)

        stack.append(index)

    return result


if __name__ == "__main__":
    print(stock_span(array("B", [100, 80, 60, 70, 60, 75, 85])))
    print(stock_span_efficient(array("B", [100, 80, 60, 70, 60, 75, 85])))
