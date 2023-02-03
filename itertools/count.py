import itertools as it

# Use count, when you dont know the number of items 
# to generate running numbers for them 

# example 1
letters = "ABCDEFG"
for c,n in zip(letters, it.count(100,-1)):
    print(c, n)
