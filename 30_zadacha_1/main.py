from functools import reduce
from typing import List


def my_mult(a: int, b: int) -> int:

    result = a * b

    print(f"{a} * {b} = {result}")

    return result


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]

names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]

numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]


if __name__ == "__main__":
    biggest_floats: List[float] = list(map(lambda x: round(x ** 3, 2), floats))
    large_names: List[str] = list(filter(lambda name: len(name) >= 5, names))
    print(biggest_floats)
    print(large_names)
    multiply = reduce(my_mult, numbers)
    print(multiply)
