"""
return a new sorted merged list from K sorted lists, each with size N
"""


# naive solution: O(knlog(kn))
def merge_sorted_lists(arrays, k):
    """Merge k arrays 

    Args:
        arrays ([type]): [description]
        k ([type]): [description]

    Returns:
        [type]: [description]
    """
    res = []

    for arr in arrays:
        res.extend(arr)

    return sorted(res)
