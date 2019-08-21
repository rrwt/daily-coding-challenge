"""
Assume you have access to a function toss_biased() which returns 0 or 1
with a probability that's not 50-50 (but also not 0-100 or 100-0).
You do not know the bias of the coin.
"""
import random


def toss_biased() -> int:
    return random.randint(0, 1)


def toss_unbaised():
    """
    toss 2 times:
        assign 0-1 = 0
        assign 1-0 = 1
        discard 0-0 and 1-1
    """
    while True:
        first, second = toss_biased(), toss_biased()

        if first == 0 and second == 1:
            return 0
        if first == 1 and second == 0:
            return 1


if __name__ == "__main__":
    print(toss_unbaised())
