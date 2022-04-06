'''
Array is given which is consists of positive numbers.
always start with idx 0 and jump to dix 1. 
if nums[n-i-1] > nums[n-i] then stick with [n-i-1] so that I can jumps more. 

'''

# def canJump(nums):
#     z = len(nums)-1
#     if len(nums) == 1:
#         return True
#     for i in range(0, z):
#         if nums[i] < z:
#             z = z-1
#     return True if z != 0 else False


        
a = [2,3,1,1,4]
b = [3,2,1,0,4]
c = [0]
# print(canJump(c))

def canJump0(nums):
    n = len(nums)
    if n <= 1:
        return True
    dp = [True] + [False]*(n-1)
    for i in range(1,n):
        dp[i] = any(nums[j] >= (i-j) for j in range(i) if dp[j])
    return dp[n-1]

    '''
    dynamic programming
    time complexity is O(n^2)
    '''

def canJunp1(nums):
    goal = len(nums) -1
    for i in range(len(nums) -1, -1, -1):
        print(i, nums[i])
        if i + nums[i] >= goal:
            goal = i
    return True if goal == 0 else False

'''
time complexity is O(n)
space complexity is O(1).
'''

# print(canJunp1(a))