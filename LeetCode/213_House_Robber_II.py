
def helper(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n+rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

def rob(nums):
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


a = [2,3,2]
a = [1,2,3,1]
a = [1,2,3]

print(rob(a))