
def threeSum(nums):
    ans = []
    nums.sort()

    for idx, val in enumerate(nums):
        if idx > 0 and val == nums[idx - 1]:
            continue
        l, r = idx+1, len(nums)-1
        while l < r:
            sum = val + nums[l] + nums[r]
            if sum > 0:
                r += -1
            elif sum < 0:
                l += 1
            else: 
                ans.append([val, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return ans





a = [-1,0,1,2,-1,-4]
b = []
c = [0]
print(threeSum(a))

# Time Complexity: O(nlogn) + O(n^2) = O(n^2)
# Space Complexity: O(1) 