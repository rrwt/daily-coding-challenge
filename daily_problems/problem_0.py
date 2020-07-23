import heapq
import functools


"""
return a new sorted merged list from K sorted lists, each with size N
"""


# naive solution: O(knlog(kn))
def merge_sorted_lists(arrays):
    """Merge k arrays

    Args:
        arrays (list): A list of list

    Returns:
        list: flattened and sorted list
    """
    res = []

    for arr in arrays:
        res.extend(arr)

    return sorted(res)


def merge_sorted_lists_min_heap(arrays):
    """An approach to efficiently merge k arrays using min heap.
    This approach takes advantage of the fact that all the arrays
    are sorted.

    Time complexity: O(Kn)
    Time taken to create and merge a min heap is proportional to number of elements

    Args:
        arrays (list): A list of list
        k (integer): Number of lists

    Returns:
        list: flattened and sorted list
    """
    # TODO: Resolve without using built in heap
    return list(heapq.merge(*arrays))


def merge_sorted_merge_sort_algorithm(arrays):
    """Merge the sorted arrays using merge part of merge sort.
    time complexity: O(kn)
    space complexity: O(nk)

    Args:
        arrays (list): A list of list
        k (integer): Number of lists

    Returns:
        list: flattened and sorted list
    """
    arr_len = len(arrays[0])

    def merge(a, b):
        a_len = len(a)
        i = 0
        j = 0
        res = []

        while i < a_len and j < arr_len:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        if i < a_len:
            res.extend(a[i:])

        if j < arr_len:
            res.extend(b[j:])

        return res

    return functools.reduce(merge, arrays)
