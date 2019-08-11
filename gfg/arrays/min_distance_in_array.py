"""
Given an unsorted array arr[] and two numbers x and y,
find the minimum distance between x and y in arr[].
The array might also contain duplicates.
You may assume that both x and y are different and present in arr[].
"""
import random


def min_distance(arr: list, x: int, y: int) -> int:
    index = 0
    while arr[index] not in (x, y):
        index += 1

    last_index: int = index
    min_dist: int = len(arr)

    for ind in range(index + 1, len(arr)):
        if arr[ind] == arr[last_index]:
            last_index = ind
        elif arr[ind] in (x, y):
            min_dist = min(min_dist, ind - last_index)
            last_index = ind

    return min_dist


if __name__ == "__main__":
    for _ in range(10):
        arr = [random.randint(1, 100) for _ in range(10)]
        x, y = random.choices(arr, k=2)

        while y == x:
            y = random.choice(arr)

        print(
            "Given",
            arr,
            "and two integers",
            x,
            "and",
            y,
            "the min distance between them is",
            min_distance(arr, x, y),
        )

