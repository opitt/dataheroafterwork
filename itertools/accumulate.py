import itertools as it
import random
from operator import sub

nums = [random.randint(0, 100) for _ in range(20)]
print(*nums)

print(*it.accumulate(nums, func=sub))

print(*it.accumulate(nums, func=lambda a,b: a%b))
