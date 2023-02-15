import itertools as it

new_list = list(it.dropwhile(5,[1,4,6,3,4,8,1]))
print(new_list)