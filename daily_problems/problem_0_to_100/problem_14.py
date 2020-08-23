"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
"""
import math
from random import random


def monte_carlo_pi():
    """
    area of a circle of radius .5 = .25*PI. Area of square of side 1 = 1
    The square will contain the circle 100%.
    If we randomly generate 1000s of points within the square, we can say that
    the ratio of points withing the circle and total number of points is going to
    be the ratio of area of circle to that of rectangle
    """
    inside: int = 0

    for i in range(1_000_000):
        x = random()
        y = random()
        distance = math.sqrt(pow(abs(0.5 - x), 2) + pow(abs(0.5 - y), 2))
        if distance <= 0.5:
            inside += 1

    print(4 * inside / 1_000_000)


if __name__ == "__main__":
    monte_carlo_pi()
