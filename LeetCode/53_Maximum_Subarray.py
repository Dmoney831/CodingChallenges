def maxSubArray(nums):
    max_sub = 0
    sum = 0

    for i in nums:
        if sum < 0:
            sum = 0
        sum += i
        # print(sum)
        max_sub = max(max_sub, sum)
    return max_sub 

def maxSubArray(nums):
    max_sub = 0
    total = 0
    for i in nums:
        if total < 0:
            total = 0
        total += i
        max_sub = max(total, max_sub)
    return max_sub

a = [-2,1,-3,4,-1,2,1,-5,4]
b = [1]
c = [5,4,-1,7,8]
d = [-1, -4, -5, -3, -7]

print(maxSubArray(a))
# ********Time Complexity: Big O(n)