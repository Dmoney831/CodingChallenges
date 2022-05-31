from collections import Counter

def topKFrequent(nums, k):
    count = {}
    freq = [ [] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # print(count.get(n, 0))
    print(count)
    for n, c in count.items():
        print(n,c)
        freq[c].append(n)
    print(freq)

    res = []
    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    # print(res)


# make a dictionary that continas keys and values.
# sort dictionary by value's size.
# get the last two of the keys.

def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    print(count)
    res = dict(sorted(count.items(), key=lambda item: item[1]))
    print(res)
    ans = list(res.keys())
    print(ans)
    print(ans[-k:])
    
import collections
def topKFrequent(nums, k):
    count = {}
    for i in nums:
        if i not in count:
            count[i] = 1 + count.get(i, 0)
        else:
            count[i] += 1
    res = dict(sorted(count.items(), key=lambda item: item[1]))
    ans = list(res.keys())
    print(ans)
    print(ans[-k:])
    print(res)
    print(count)

import heapq
import collections
def topKFrequent(nums, k):
    res = []
    dict = collections.Counter(nums)
    for val, count in dict.items():
        if len(res) < k:
            heapq.heappush(res, (count, val))
        else:
            heapq.heappush(res, (count, val))
            heapq.heappop(res)
    print([val for count, val in res])
    

def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    count = dict(sorted(count.items(), key=lambda item: item[1]))
    # count = dict(sorted(count.items())) # dict(sorted(count.items()))
    print(count)
    ans = list(count.keys())
    print(ans)
    return ans[-k:]
nums = [5,5,5,5,5,4,1,1,1,2,2,3,4,4,4,4]  
k = 2

# nums = [4,1,-1,2,-1,2,3]
# k = 2
print(topKFrequent(nums, k))
