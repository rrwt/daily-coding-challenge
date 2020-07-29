"""
Compute the running median of a sequence of numbers. That is,
given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2 1.5 2 3.5 2 2 2
"""


def running_median() -> float:
    count_num = 0
    index_med = -1
    median = None
    arr = []

    while (num := (yield median)) is not None:
        arr.append(num)
        arr.sort()
        count_num += 1

        if count_num & 1:
            index_med += 1
            median = arr[index_med]
        else:
            median = (arr[index_med] + arr[index_med+1]) / 2


if __name__ == "__main__":
    rm = running_median()
    rm.send(None)  # To put the generator in active state. alt: next(rm)
    for _ in [2, 1, 5, 7, 2, 0, 5]:
        try:
            print(rm.send(_))
        except StopIteration:
            break
