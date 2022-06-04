def threeSumClosest(nums,  target):
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j, k = i+1, len(nums)-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == target:
                return total
            if abs(total - target) < abs(res - target):
                res = total
            if total < target:
                j += 1
            elif total > target:
                k -= 1
    return res


nums, target = [-1,2,1,-4], 1
print(threeSumClosest(nums, target))

def threeSumClosest(nums, target):
    diff = float('inf')
    nums.sort()
    for i in range(len(nums)):
        lo, hi = i+1, len(nums)-1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            print(diff)
            if abs(target - sum) < abs(diff):
                diff = target - sum
            if sum < target:
                lo += 1
            else:
                hi -= 1 
        if diff == 0:
            break
    return target - diff


# Time Complexity: O(n^2). We have outer and inner loops, each going through n elements. Sorting the array takes O(nlogn), so overall complexity is O(nlogn + n^2). This is asymptotically equivalent to O(n^2). 
# Space Complexity: from O(log n) to O(n), depending on the implementation of the sorting algorithm. 
