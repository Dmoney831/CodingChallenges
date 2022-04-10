'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

'''

'''
def longestConsecutive(nums):
    x = sorted(nums)
    print(x)
    l,r = 0, len(nums)-1
    long = 0
    ans = []
    while l < r:
        if x[l]+1 == x[l+1]:
            long +=1
            l += 1
            ans.append(long)
        else:
            l += 1

    if ans is None:
        return 0
    else:
        return max(ans)+1

'''


def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1

            longest = max(length, longest)
    return longest
    
        




nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# print(max(nums))

longestConsecutive(nums)