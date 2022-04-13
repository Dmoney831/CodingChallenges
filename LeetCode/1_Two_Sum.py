# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i,j]



def twoSum(nums, target):
    hash = {}

    for i, n in enumerate(nums):
        diff = target-n
        # print(diff)
        if diff in hash:
            # print(hash[diff], i, hash)
            return [hash[diff], i]
        hash[n] = i
    return 

nums = [2,7,11,15] 
target = 9
output = [0,1]

# nums = [3,2,4] 
# target = 6
# Output= [1,2]

print(twoSum(nums, target))

