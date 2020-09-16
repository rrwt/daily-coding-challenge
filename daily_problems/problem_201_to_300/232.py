"""
Implement a PrefixMapSum class with the following methods:
    insert(key: str, value: int): Set a given key's value in the map.
        If the key already exists, overwrite the value.
    sum(prefix: str): Return the sum of all values of keys that begin
        with a given prefix.
For example, you should be able to run the following code:
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5
"""


class PrefixMapSum:
    def __init__(self):
        self.trie = {}
        self.total = 0

    def insert(self, key: str, value: int) -> None:
        if not key:
            return None

        self.total += value

        if key[0] in self.trie:
            self.trie[key[0]].insert(key[1:], value)
        else:
            sub_trie = PrefixMapSum()
            sub_trie.insert(key[1:], value)
            self.trie[key[0]] = sub_trie

    def sum(self, prefix: str) -> int:
        if not prefix:
            return self.total

        if prefix[0] in self.trie:
            if len(prefix) > 1:
                return self.trie[prefix[0]].sum(prefix[1:])
            return self.total

        return 0


if __name__ == "__main__":
    map_sum = PrefixMapSum()
    map_sum.insert("columnar", 3)
    assert map_sum.sum("col") == 3

    map_sum.insert("column", 2)
    assert map_sum.sum("col") == 5
