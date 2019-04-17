# naive solution O(n*n)
def verify_sum(ar, value):
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if ar[i] + ar[j] == value:
                return True

    return False


# more efficient solution O(n*logn)
def verify_sum_2(ar, value):
    ar.sort()
    i = 0
    j = len(ar) - 1

    while i < j:
        sum_ = ar[i] + ar[j]

        if sum_ == value:
            return True
        elif sum_ > value:
            j = j-1
        else:
            i = i+1

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
