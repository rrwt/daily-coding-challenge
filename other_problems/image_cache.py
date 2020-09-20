"""
You are to build a simple image cache for holding images in memory.
This cache should have a maximum size in bytes. Since the cache has
a limited byte size, we will use an LRU algorithm to evict based on
which URLs were least recently seen.
The format of the input file will be as follows:
1. The first line of the input will be an integer indicating the
    maximum size of the cache in bytes.
2. The second line will be an integer that indicates the number of
    URLs (N) that will appear subsequently in the input.
3. The remaining N lines of the input are URLs representing requests
    that will be made to the cache.
cache_size_in_bytes
number_of_urls
url_1
url_2
...
url_n

For each URL, your program should attempt to fetch it from the cache,
and if it isn’t present, download it from the internet and place it
in the cache. You should save the entire image in the cache, even
though you can achieve the desired output without doing so.
Your output should contain N lines, in the same order as the input.
Each line will be formatted as <url requested> <IN_CACHE|DOWNLOADED> <size of image in bytes>
If you need more images to experiment with, you can use a site like placeholder.com
For example: https://via.placeholder.com/1000x500
Sample Input
    524288
    3
    http://i.imgur.com/xGmX4h3.jpg
    http://i.imgur.com/IUfsijF.jpg
    http://i.imgur.com/xGmX4h3.jpg
Sample Output
    http://i.imgur.com/xGmX4h3.jpg DOWNLOADED 93606
    http://i.imgur.com/IUfsijF.jpg DOWNLOADED 317908
    http://i.imgur.com/xGmX4h3.jpg IN_CACHE 93606
"""
from random import randint
from time import sleep
from typing import Tuple
from requests import get, ConnectionError


class Node:
    def __init__(self, url, data: bytes) -> None:
        self.data = data
        self.size = len(data)
        self.url = url
        self.prev = None
        self.next = None


def get_next_delay(delay: int) -> int:
    return delay * randint(1, 2) + randint(1, 2)


def fetch_image(url: str, retries: int = 5) -> bytes:
    delay = 0

    for _ in range(retries):
        sleep(delay)
        delay = get_next_delay(delay)

        try:
            return get(url).content
        except ConnectionError:
            pass

    raise Exception("Unable to fetch the image")


class LRUCache:
    def __init__(self, size: int):
        self.head = self.tail = None
        self.hashmap = {}
        self.max_size = size
        self.size = 0

    def delete_tail(self) -> None:
        if not self.tail:
            return None

        tail = self.tail
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self.size -= tail.size
        del self.hashmap[tail.url]
        del tail

    def move_to_beginning(self, key: str) -> None:
        node = self.hashmap[key]

        if node == self.head:
            return None

        if node.next:
            node.next.prev = node.prev

        node.prev.next = node.next
        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def insert(self, key: str, node: Node):
        while self.tail and self.size + node.size > self.max_size:
            self.delete_tail()

        node.next = self.head

        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node

        self.size += node.size
        self.hashmap[key] = node

    def fetch(self, url: str) -> Tuple[str, str, int]:
        if url not in self.hashmap:
            image = fetch_image(url)
            node = Node(url, image)
            self.insert(url, node)
            return url, "DOWNLOADED", node.size
        else:
            self.move_to_beginning(url)
            return url, "IN_CACHE", self.hashmap[url].size


if __name__ == "__main__":
    cache_size = int(input("Input Cache Size:"))
    num_urls = int(input("Input number of URLS:"))
    cache = LRUCache(cache_size)
    res = []

    for _ in range(num_urls):
        cur_url = input("Next url: ")
        res.append(cache.fetch(cur_url))

    print()
    print(*res, sep="\n")
