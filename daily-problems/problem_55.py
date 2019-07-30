"""
Implement a URL shortener with the following methods:
  shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
  restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.
"""
import random
from typing import Optional
from string import ascii_uppercase, ascii_lowercase, digits


class URL:
    """
    Redundant url shortening service.
    If same url gets entered twice, we create 2 links for it
    """

    def __init__(self):
        self._dict = {}
        self.characters = list(ascii_uppercase + ascii_lowercase + digits)
        self.base_url = "https://www.example.com/"

    def _get_shortened_url(self) -> str:
        return "".join([random.choice(self.characters) for _ in range(6)])

    def shorten(self, url: str) -> str:
        while True:
            short_url: str = self._get_shortened_url()

            if short_url not in self._dict:
                self._dict[short_url] = url
                return self.base_url + short_url

    def restore(self, short_url: str) -> Optional[str]:
        if short_url.startswith(self.base_url):
            short_url = short_url[len(self.base_url) :]
        if short_url in self._dict:
            return self._dict[short_url]
        return None


if __name__ == "__main__":
    url = URL()
    duck: str = "https://www.duckduckgo.com"
    first = url.shorten(duck)
    proton: str = "https://protonmail.com"
    second = url.shorten(proton)
    print(first)
    print(second)
    assert url.restore(first) == duck
    assert url.restore(second) == proton
