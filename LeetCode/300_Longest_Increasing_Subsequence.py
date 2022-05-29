# Dynamic Programming
def lengthOfLIS(nums):
    LIS = [1]*len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        # print(nums[i])
        for j in range(i+1, len(nums)):
            # print(nums[j])
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])

    return max(LIS) 

def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            # print(nums[i], nums[j], dp[i], dp[j])
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    # print(nums)
    # print(dp)
    return max(dp)

a = [10,9,2,5,3,7,101,18]
# a = [0,1,0,3,2,3]
# a = [7,7,7,7,7,7,7]
print(lengthOfLIS(a))
