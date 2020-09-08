"""
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.
For example,
    given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
    your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
"""
from random import random
from typing import List


def get_probability(numbers: List[int], sum_arr: List[float]) -> int:
    prob = random()

    for index, value in enumerate(sum_arr):
        if prob <= value:
            return numbers[index]

    return numbers[-1]


def generate_probability_sum(probabilities: List[float]) -> List[float]:
    return [
        prob if index == 0 else prob + probabilities[index - 1]
        for index, prob in enumerate(probabilities)
    ]


if __name__ == "__main__":
    probability_sum = generate_probability_sum([0.1, 0.5, 0.2, 0.2])
    nums = [1, 2, 3, 4]
    count = 0

    for _ in range(1_000_000):
        if get_probability(nums, probability_sum) == 1:
            count += 1

    # around 10 %
    assert count / 1_000_000 < 0.11, "probability of 1 is " + str(count / 1_000_000)
