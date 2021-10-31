import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
list_compl: float = timeit.timeit('"-".join([str(x) for x in range(0, 100)])', number=10000)
map_compl: float = timeit.timeit('"".join(list(map(lambda x, y: x + y, [str(x) for x in range(0, 100)], ["-" for _ in range(0, 100)])))', number=10000)


print(res)
print(list_compl)
print(map_compl)

