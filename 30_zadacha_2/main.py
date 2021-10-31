import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
list_compl: float = timeit.timeit('"-".join(str(x) for x in range(0, 100))', number=10000)
map_try: float = timeit.timeit('map')

x = list(map("-".join(), [str(x) for x in range(0, 100)]))

print(res)
print(list_compl)


