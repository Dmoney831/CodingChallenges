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



nums = [1,1,1,2,2,3]  
k = 2

# nums = [4,1,-1,2,-1,2,3]
# k = 2
topKFrequent(nums, k)
