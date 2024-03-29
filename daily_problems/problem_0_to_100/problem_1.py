"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


# naive solution O(n*n) & O(1)
def verify_sum(ar, value):
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[i] + ar[j] == value:
                return True

    return False


# more efficient solution O(n*log(n)) & O(1)
def verify_sum_2(ar, value):
    ar.sort()
    i = 0
    j = len(ar) - 1

    while i < j:
        sum_ = ar[i] + ar[j]

        if sum_ == value:
            return True
        elif sum_ > value:
            j = j - 1
        else:
            i = i + 1

    return False


# Using sets. most efficient O(n) & O(n)
def verify_sum_3(ar, value):
    s = set()

    for el in ar:
        if value - el in s:
            return True
        else:
            s.add(el)

    return False


if __name__ == "__main__":
    import random

    for _ in range(1000_000):
        arr = random.sample(range(1, 1000_000), 10)
        k = random.randint(100, 1000_000)

        if verify_sum(arr, k) != verify_sum_2(arr, k):
            """a test to verify that everything is working fine in the efficient solution"""
            print(arr)
            print(k)
            break
