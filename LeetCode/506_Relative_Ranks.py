def findRelativeRanks(score):
    sort = sorted(score)[::-1]
    # print(sort)
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score)+1)]
    # print(rank)
    # print(list( map(dict(zip(sort, rank)).get, score) ))
    print(( dict(zip(sort, rank)) ))
    return list(map(dict(zip(sort, rank)).get, score))




score = [5,4,3,2,1]
# Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
print(findRelativeRanks(score))


def findRelativeRanks(self, nums):
    sort = sorted(nums)[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score)+1)]
    return map(dict(zip(sort, rank)).get, nums)