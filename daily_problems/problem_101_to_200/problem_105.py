"""
Given a function f, and N return a debounced f of N milliseconds.

That is, as long as the debounced f continues to be invoked,
f itself will not be called for N milliseconds.
"""
from time import sleep, time
from datetime import datetime
from typing import Optional


def debounce(milliseconds: int):
    """
    Debouncing is a programming practice used to ensure that
    time-consuming tasks do not fire so often. In other words,
    it limits the rate at which a function gets invoked.
    """
    def decorator(func):
        start: Optional[time] = None

        def wrapper(*args, **kwargs):
            nonlocal start
            end = time()

            if start is None or (end - start) >= milliseconds / 1000:
                # start = None -> first call
                # end - start -> time diff between 2 calls
                result = func(*args, **kwargs)
                start = time()
                return result

            return False

        return wrapper

    return decorator


@debounce(3000)
def f() -> bool:
    print("Invoked at", datetime.now())
    return True


if __name__ == "__main__":
    assert f() is True
    assert f() is False
    sleep(1)
    assert f() is False
    sleep(1)
    assert f() is False
    sleep(1)
    assert f() is True
