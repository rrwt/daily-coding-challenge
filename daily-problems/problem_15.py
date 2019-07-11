"""
Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.
"""
from random import randint


def reservior_sampling(item: int, count: int, res: int) -> int:
    """
    when there is only one item, return it.
    probability of choosing an item from a sample of i items = 1/i
    probability of choosing ith item  = 1/i
    in case the random index = 1/i, that would mean the ith item was
    chosen fairly. Replace current choice with the ith one.
    Everytime we get a new item, we check whether this item is going to be
    the one (being selected).
    """
    if count == 0:
        return item

    index: int = randint(0, count)

    if index == count - 1:
        return item

    return res


if __name__ == "__main__":
    res = -1
    for i in range(100):
        res = reservior_sampling(randint(1, 1_000_000), i, res)
    print(res)
