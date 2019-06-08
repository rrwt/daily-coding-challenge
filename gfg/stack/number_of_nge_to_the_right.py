"""
Given an array of n integers and q queries, print the number of next greater
elements to the right of the given index element.
Input : a[] = {3, 4, 2, 7, 5, 8, 10, 6}  
              q = 2 
              index = 0, 
              index = 5
Output: 4 
        1 
Explanation: the next greater elements
to the right of 3(index 0) are 4, 7, 8, 
10. The next greater elements to the right
of 8(index 5) are 10.
"""


def nge_to_the_right(elements: list) -> list:
    """
    Solution: Iterate over the list in reverse and store nge for each
    time complexity: O(n)
    space complexity: O(n)
    time complexity to answer queries (what's nge for this index) = O(1) (afterwards)
    """
    l: int = len(elements)
    stack: list = [l - 1]
    result: list = [0] * l
    index: int = l - 2

    for i in range(l - 2, -1, -1):
        while stack and elements[i] >= elements[stack[-1]]:
            stack.pop()

        if stack:
            result[index] = result[stack[-1]] + 1

        stack.append(index)
        index -= 1

    return result


if __name__ == "__main__":
    print(nge_to_the_right([3, 4, 2, 7, 5, 8, 10, 6]))
