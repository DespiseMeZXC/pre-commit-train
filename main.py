#!/usr/bin/env python3


def some_function(a, b):
    """Функция с неправильным форматированием, чтобы протестировать линтеры"""
    x = 1 + 2
    if x > 10:
        print("x больше 10")

    return a + b


class BadlyFormattedClass:
    def __init__(self, name):
        self.name = name

    def some_method(self, x):
        print(f"Hello, {self.name}, value: {x}")


if __name__ == "__main__":
    result = some_function(1, 2)
    print(result)
    obj = BadlyFormattedClass("Test")
    obj.some_method(42)
