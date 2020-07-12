# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
# By convention, 1 is included.


def ugly_number(n: int) -> int:
    # find nth ugly number
    ugly = [0] * n
    ugly[0] = 1
    index_2 = index_3 = index_5 = 0
    next_multiplier_of_2 = 2
    next_multiplier_of_3 = 3
    next_multiplier_of_5 = 5

    for index in range(1, n):
        ugly[index] = min(next_multiplier_of_2, next_multiplier_of_3, next_multiplier_of_5)

        if ugly[index] == next_multiplier_of_2:
            index_2 += 1
            next_multiplier_of_2 = ugly[index_2] * 2
        if ugly[index] == next_multiplier_of_3:
            index_3 += 1
            next_multiplier_of_3 = ugly[index_3] * 3
        if ugly[index] == next_multiplier_of_5:
            index_5 += 1
            next_multiplier_of_5 = ugly[index_5] * 5

    return ugly[n-1]


if __name__ == "__main__":
    for i in range(1, 20):
        print(ugly_number(i))
