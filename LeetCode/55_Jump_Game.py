def canJump(nums):
    jump = 0
    for idx, num in enumerate(nums):
        print(f'idx: {idx}, num: {num}, jump: {jump}')
        if idx > jump:
            return False
        jump = max(jump, idx + num)
    return True

        
nums = [2,3,1,1,4] # True
# nums = [3,2,1,0,4] # False
# nums = [0] # True
print(canJump(nums))

# def canJump0(nums):
#     n = len(nums)
#     if n <= 1:
#         return True
#     dp = [True] + [False]*(n-1)
#     for i in range(1,n):
#         dp[i] = any(nums[j] >= (i-j) for j in range(i) if dp[j])
#     return dp[n-1]

'''
dynamic programming
time complexity is O(n^2)
'''

# def canJunp1(nums):
#     goal = len(nums) -1
#     for i in range(len(nums) -1, -1, -1):
#         print(i, nums[i])
#         if i + nums[i] >= goal:
#             goal = i
#     return True if goal == 0 else False

'''
time complexity is O(n)
space complexity is O(1).
'''

# print(canJunp1(a))