import heapq


"""
return a new sorted merged list from K sorted lists, each with size N
"""


# naive solution: O(knlog(kn))
def merge_sorted_lists(arrays):
    """Merge k arrays

    Args:
        arrays (list): A list of list
        k (integer): Number of lists

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

    Time complexity: Kn
    Time taken to create and merge a min heap is proportional to number of elements

    Args:
        arrays (list): A list of list
        k (integer): Number of lists

    Returns:
        list: flattened and sorted list
    """
    return list(heapq.merge(*arrays))
