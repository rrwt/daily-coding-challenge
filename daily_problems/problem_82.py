"""
Using a read7() method that returns 7 characters from a file,
implement readN(n) which reads n characters.

For example,
    given a file with the content "Hello world",
    three read7() returns "Hello w", "orld" and then "".
"""


class FileReader:

    def __init__(self, content: str) -> None:
        self.content = content
        self.index = 0
        self.length = len(content)

    def read7(self) -> str:
        if self.index + 7 < self.length:
            res = self.content[self.index:self.index + 7]
            self.index += 7
        else:
            res = self.content[self.index:]
            self.index = self.length

        return res

    def read_n(self, n: int) -> str:
        char_count = 0
        buffer = ""
        res = ""

        while self.index < self.length:
            if char_count >= n:
                res = buffer[:n]
                buffer = buffer[n:]
                char_count -= n
            else:
                buffer += self.read7()
                char_count += 7

            if res:
                yield res
                res = ""

        if buffer and self.index >= self.length:
            yield buffer


if __name__ == '__main__':
    f = FileReader("Hello World")
    assert f.read7() == "Hello W"
    assert f.read7() == "orld"
    assert f.read7() == ""

    f = FileReader("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                   "tempor incididunt")
    gen = f.read_n(20)
    assert next(gen) == "Lorem ipsum dolor si"
    assert next(gen) == "t amet, consectetur "
    assert next(gen) == "adipiscing elit, sed"
    assert next(gen) == " do eiusmod tempor i"
    assert next(gen) == "ncididunt"

    try:
        next(gen)
    except StopIteration:
        pass
