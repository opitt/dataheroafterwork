import itertools as it

a = [1,2,3,4]
b = [6,5,4,3,2,1]

for a, b in it.zip_longest(a,b, fillvalue=0):
  print(a,b,a+b)
