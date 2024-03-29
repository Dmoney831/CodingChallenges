def fourSum(nums, target):
    def kSum(nums, target, k):
        res = []
        if not nums:
            return res
        average_value = target // k
        if average_value < nums[0] or nums[-1] < average_value:
            return res
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in kSum(nums[i+1:], target - nums[i], k-1):
                    res.append([nums[i]] + subset)
        return res
    
    def twoSum(nums, target):
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
    nums.sort()
    return kSum(nums, target, 4)


nums, target = [1,0,-1,0,-2,2], 0
# nums, target = [2,2,2,2,2], 8

print(fourSum(nums, target))

# Time Complexity: O(n^(k-1)). we have k-2 loops iterating over n elements, and twoSum is O(n). Note that for k > 2, sorting the array does not change the overall time complexity.
# Space Complexity: O(n) for the hash set. The space needed for the recursion will not exceed O(n).