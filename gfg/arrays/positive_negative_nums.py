"""
An array contains both positive and negative numbers in random order.
Rearrange the array elements so that positive and negative numbers are
placed alternatively.
    - Number of positive and negative numbers need not be equal.
    - If there are more positive numbers they appear at the end of the array.
    - If there are more negative numbers, they too appear in the end of the array.

For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9],
then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]
"""


def alternate_numbers(arr: list) -> list:
    positive, negative, = 0, 1
    l: int = len(arr)

    while all((positive < l, negative < l)):
        while positive < l and arr[positive] >= 0:
            positive += 2
        while negative < l and arr[negative] < 0:
            negative += 2

        if all((positive < l, negative < l)):
            arr[positive], arr[negative] = arr[negative], arr[positive]

    if positive < l:
        while positive < l and arr[positive] >= 0:
            positive += 2
        k = positive + 2

        while k < l:
            if arr[k] >= 0:
                arr[k], arr[positive] = arr[positive], arr[k]
                positive += 2
            k += 2

    if negative < l:
        while negative < l and arr[negative] < 0:
            negative += 2
        k = negative + 2

        while k < l:
            if arr[k] < 0:
                arr[k], arr[negative] = arr[negative], arr[k]
                negative += 2
            k += 2

    return arr


def alternate_numbers_2(arr: list) -> list:
    def validate_condition(index) -> bool:
        return (index % 2 == 0 and arr[index] >= 0) or (
            index % 2 == 1 and arr[index] < 0
        )

    def have_same_sign(a: int, b: int) -> bool:
        return all((a >= 0, b >= 0)) or all((a < 0, b < 0))

    i, l = 0, len(arr)

    while i < l:
        if not validate_condition(i):
            j = i + 1

            while j < l and have_same_sign(arr[i], arr[j]):
                j += 1

            if j < l:
                arr[i], arr[j] = arr[j], arr[i]
        i += 1

    return arr


if __name__ == "__main__":
    print(alternate_numbers([-1, 2, -3, 4, 5, 6, -7, 8, 9, -10]))
    print(alternate_numbers([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
    print(alternate_numbers_2([-1, 2, -3, 4, 5, 6, -7, 8, 9, -10]))
    print(alternate_numbers_2([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))
