'''
iterate over the index and check the every other index position.
if value nums[2] < nums[3], select nums[3].
'''

def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
        print(f'n: {n}, temp: {temp}, rob1: {rob1}, rob2: {rob2}')
    return rob2         
    

# a = [1,2,3,1]
a = [2,7,9,3,1]

rob(a)

# #####################
def rob_v2(nums):
    if not nums:
        return 0

    if len(nums) <=2:
        return max(nums)
    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for x in range(2, len(nums)):
        dp[x] = max(dp[x-1], nums[x]+dp[x-2])
    return dp[-1]