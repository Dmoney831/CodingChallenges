# Binary Search
import math
def minEatingSpeed(piles, h):
    l, r = 1, max(piles)
    result = r

    while l <= r:
        k = (l + r) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        if hours <= h:
            result = min(result, k)
            r = k - 1
        else:
            l = k + 1
    return result



piles = [3,6,7,11]  
h = 8
piles = [30,11,23,4,20]  
h = 5
piles = [30,11,23,4,20]  
h = 6

print(minEatingSpeed(piles, h))