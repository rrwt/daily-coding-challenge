"""
Given a sorted dictionary (array of words) of an alien language,
find order of characters in the language.
"""
from .ds import GraphM  # type: ignore
from .topological_sort import topological_sort_using_dfs  # type: ignore


def order_of_characters(words: tuple, num_char: int) -> list:
    """
    Order can be found using a DAG.
    The dictionary is sorted, therefore we can compare characters of each word to form DAG.
    Afterwords topological sorting can be applied to find the final order
    """
    length = len(words)
    graph = GraphM(num_char, "directed")

    for i in range(length - 1):
        for c1, c2 in zip(words[i], words[i + 1]):
            if c1 != c2:
                graph.add_edge(ord(c1) - 97, ord(c2) - 97)
                break

    return topological_sort_using_dfs(graph.graph, num_char)


if __name__ == "__main__":
    print(list(map(lambda x: chr(x + 97),
                   order_of_characters(("baa", "abcd", "abca", "cab", "cad"), 4))))
