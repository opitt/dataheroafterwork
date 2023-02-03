# Exploring itertools zip_longest function

import itertools as it

a = [1,2,3,4]
b = [6,5,4,3,2,1]

for a, b in it.zip_longest(a,b, fillvalue=0):
  print(a,b,a+b)

# Example 2
c = [1,2,3,4,5]
d = [6,7,8,9,10,11,12,4]
print([sum(s) for s in it.zip_longest(c,d,fillvalue=0)])