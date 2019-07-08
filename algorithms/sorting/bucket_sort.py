"""
Bucket Sort: Linear time sorting algorithm when input array is uniformly distributed
Time complexity: O(n) - average, O(n*n) - worst
Space Complexity: O(n*k) where k = number of buckets

- Create a k bucket array and then calculate the index of each array element.
- Append the element at the end of the bucket.  (Scatter)
- Sort each bucket using some other sorting technique
- Concatenate the buckets. (gather)
"""


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        j = i
        el = arr[j]

        while j > 0 and el < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = el

    return arr


def bucket_sort(arr: list) -> list:
    buckets: int = 10  # assuming 10 buckets, each of 0.1 capacity
    bucket_arr: list = [[] for _ in range(buckets)]

    for element in arr:
        index = int(element * buckets)
        bucket_arr[index].append(element)

    bucket_arr[0] = insertion_sort(bucket_arr[0])

    for i in range(1, buckets):
        bucket_arr[0].extend(insertion_sort(bucket_arr[i]))

    return bucket_arr[0]


if __name__ == "__main__":
    print(bucket_sort([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]))
