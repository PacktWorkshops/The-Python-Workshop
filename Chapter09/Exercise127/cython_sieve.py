import timeit

print(timeit.timeit('list(PrimesBelow(1000))', setup='from sieve_module import PrimesBelow', number=10000))
