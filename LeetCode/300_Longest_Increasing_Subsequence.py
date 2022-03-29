# Dynamic Programming
def lengthOfLIS(nums):
    LIS = [1]*len(nums)
    
    for i in range(len(nums)-1,-1,-1):
        print(nums[i])
        for j in range(i+1, len(nums)):
            # print(nums[j])
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)



a = [10,9,2,5,3,7,101,18]
# a = [0,1,0,3,2,3]
# a = [7,7,7,7,7,7,7]
print(lengthOfLIS(a))
