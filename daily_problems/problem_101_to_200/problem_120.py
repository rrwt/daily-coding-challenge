"""
Implement the singleton pattern with a twist. First, instead of storing one instance,
store two instances. And in every even call of getInstance(), return the first instance
and in every odd call of getInstance(), return the second instance.
"""


class Singleton:
    __instance_1 = None
    __instance_2 = None
    __next_instance = False

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls) -> "Singleton":
        if cls.__instance_1 is None:
            cls.__instance_1 = cls.__new__(cls)
        elif cls.__instance_2 is None:
            cls.__instance_2 = cls.__new__(cls)

        if cls.__next_instance is False:
            cls.__next_instance = True
            return cls.__instance_1
        else:
            cls.__next_instance = False
            return cls.__instance_2


if __name__ == "__main__":
    s1 = Singleton.instance()
    s2 = Singleton.instance()

    for i in range(10):
        if i & 1:
            assert Singleton.instance() == s2
        else:
            assert Singleton.instance() == s1
