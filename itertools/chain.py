from itertools import chain

a=range(10)
b=range(5)

for i, n in enumerate(chain(a,b,a)):
    # Used for treating consecutive sequences as a single sequence.
    print(i, n)

for i, n in enumerate(chain.from_iterable([a,b,a])):
    # Gets chained inputs from a single iterable argument that is evaluated lazily.
    print(i, n)

squares = [n*n for n in chain(a,b,a)]
print(squares)
