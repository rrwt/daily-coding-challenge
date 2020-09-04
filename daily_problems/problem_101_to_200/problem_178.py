"""
Alice wants to join her school's Probability Student Club.
Membership dues are computed via one of two simple probabilistic games.
The first game: roll a die repeatedly.
Stop rolling once you get a five followed by a six.
Your number of rolls is the amount you pay, in dollars.
The second game: same, except that the stopping condition is a five followed by a five.
Which of the two games should Alice elect to play? Does it even matter?
Write a program to simulate the two games and calculate their expected value.
"""
from random import randint
from typing import Tuple


def dice_throw_game(game: Tuple[int, int]) -> int:
    """
    5-6 is better than 5-5.
    Reason: After getting the first 5, you have 1/6 chance each of getting a 5 or a 6.
        But in case of 5-6, even if you get another 5, you have 1/6 chance of getting
        a 6 in the third throw as second throw gets converted to the first one.
        This is not possible in case of 5-5.
    """
    throws = 0

    while True:
        while randint(1, 6) != 5:
            throws += 1

        while True:
            next_val = randint(1, 6)
            throws += 1

            if next_val == game[1]:
                return throws + 1
            elif next_val == game[0]:
                continue
            else:
                break


if __name__ == "__main__":
    # this averaged around 32 in all of the runs
    count_5_6 = 0
    for _ in range(1000):
        count_5_6 += dice_throw_game((5, 6))

    print(f"for 5-6 game and 1000 tries, average attempts are: {count_5_6 / 1000}")

    # this averaged around 36
    count_5_5 = 0
    for _ in range(1000):
        count_5_5 += dice_throw_game((5, 5))

    print(f"for 5-5 game and 1000 tries, average attempts are: {count_5_5 / 1000}")
