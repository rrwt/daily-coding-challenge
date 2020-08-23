"""
Given a function that generates perfectly random numbers between 1 and k (inclusive),
where k is an input,
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.
Hint: Make sure each one of the 52! permutations of the deck is equally likely.
"""
from random import randint
from typing import List


def shuffle(k: int) -> List[int]:
    """
    fisher-yates shuffle algorithm can be applied to generate random sequence
    """
    deck = list(range(1, 53))

    for card in range(52):
        index = randint(1, k)
        deck[index], deck[card] = deck[card], deck[index]

    return deck


if __name__ == "__main__":
    print(shuffle(randint(1, 52)))
