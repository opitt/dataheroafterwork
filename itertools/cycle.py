import itertools as it
start = 1000
prefix = "ABC"
n = 20
ids = [a+str(b) for a,b,c in zip(it.cycle(prefix),it.count(start),range(n))]
print(ids)