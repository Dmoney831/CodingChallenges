def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return left 
    

nums = [1,3,5,6]
target = 5
# output = 2

nums = [1,3,5,6]
target = 2
# output: 1

# nums = [1,3,5,6]
# target = 7
# # output: 4

nums = [2,3,5,6,9]
target = 7


print(searchInsert(nums, target))