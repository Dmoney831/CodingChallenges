def missingNumber(nums):
    ans = len(nums)
    for i in range(len(nums)):
        ans += (i - nums[i])
    print(ans)


def missingNumber(nums):
    n = len(nums)
    return (n * (n+1)) / 2 - sum(nums)


a = [3,0,1]
a = [0,1,2,3,4]
a = [0,1]
# a = [0]
# a = [1]
# a = [9,6,4,2,3,5,7,0,1]
print(missingNumber(a))
