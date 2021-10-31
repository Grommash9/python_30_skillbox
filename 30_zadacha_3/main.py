from typing import List

strings: List[str] = ['a', 'b', 'c', 'd', 'e']

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(map(lambda s, n: (s, n), strings, numbers))
print(result)
