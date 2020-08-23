"""
You have n fair coins and you flip them all at the same time.
Any that come up tails you set aside.
The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?

Write a function that, given n,
returns the number of rounds you'd expect to play until one coin remains.
"""
import math


def num_coin_flips(n: int) -> int:
    """
    After each throw, we have 50% chances of head and 50% chances of tail for each coin.
    Assuming 50% of the coin result in head, it means after each throw, we have to throw
    half of the coins again, and so on until only one coin remains.
    We can take lg of number of coins to determine the number of throws to reach 1 coin.
    ceil will provide an upper limit
    """
    return 0 if n <= 1 else math.ceil(math.log(n, 2))


if __name__ == "__main__":
    assert num_coin_flips(0) == 0
    assert num_coin_flips(1) == 0
    assert num_coin_flips(2) == 1
    assert num_coin_flips(100) == 7
    assert num_coin_flips(32) == 5
    assert num_coin_flips(500) == 9
    assert num_coin_flips(1000) == 10
