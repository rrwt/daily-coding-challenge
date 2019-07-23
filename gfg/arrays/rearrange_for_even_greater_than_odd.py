"""
Rearrange array such that arr[i] >= arr[j], if i is even,
                      and arr[i] <= arr[j], if i is odd and j < i
"""


def rearrange(arr: list) -> list:
    """Copy, Sort and fill
    Time Complexity: O(n*log(n))
    Space Complexity: O(n)
    """
    temp: list = sorted(arr)
    l: int = len(arr)
    even: int = int(l / 2)
    odd: int = even + 1
    j: int = odd - 1

    for k in range(0, l, 2):  # odd positions
        arr[k] = temp[j]
        j -= 1

    j = odd

    for k in range(1, l, 2):  # even positions
        arr[k] = temp[j]
        j += 1

    return arr


if __name__ == "__main__":
    assert rearrange([1, 2, 3, 4, 5, 6, 7]) == [4, 5, 3, 6, 2, 7, 1]
