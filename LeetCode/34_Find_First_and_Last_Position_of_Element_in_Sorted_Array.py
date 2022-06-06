def searchRange(nums, target):
    res = []
    # iterate through the array, nums, and stop if val is bigger than target
    if not nums:
        return [-1, -1]
    i = 0
    while nums[i] <= target:
        if nums[i] != target:
            i += 1
        else:
            res.append(i)
            i += 1
    return [-1, -1] if not res else res

# We need to use O(log n) runtime.

def searchRange(nums, target):
    res = []
    if not nums:
        return [-1, -1]
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            res.append(mid)
            left = mid + 1
            
    print(res)
    return [-1, -1] if not res else res 
# This is not going to work since we need to return multiple values

def searchRange(nums, target):
    def search(lo, hi):
        if nums[lo] == target == nums[hi]:
            return [lo, hi]
        if nums[lo] <= target <= nums[hi]:
            mid = (lo+hi) // 2
            left, right = search(lo, mid), search(mid+1, hi)
            return max(left, right) if -1 in left + right else [left[0], right[1]]
        return [-1, -1]
    return search(0, len(nums)-1)


nums, target = [5,7,7,8,8,10], 8
# nums, target = [5,7,7,8,8,10], 6
# nums, target = [], 0

print(searchRange(nums, target))
