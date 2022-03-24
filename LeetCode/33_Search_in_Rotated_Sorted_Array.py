def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        middle = (left + right)//2
        if target == nums[middle]:
            return middle
        # left sorted portion
        if nums[left] <= nums[middle]:
            if target > nums[middle] or target < nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        # right sorted portion
        else:
            if target < nums[middle] or target > nums[right]:
                right = middle - 1
            else:
                left = middle + 1 
    return -1
        


# a = [4,5,6,7,0,1,2] 
# b = 0

# a = [4,5,6,7,0,1,2] 
# b = 3

a = [1]
b = 0

print(search(a,b))

# def search(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left <= right:
#         middle = (left + right)//2
#         if target == nums[middle]:
#             return middle
#         # left sorted
#         if target > nums[middle] or target < nums[left]:
#             left = middle + 1
#         else:
#             right = middle -1
#         # right sorted
#         if target < nums[middle] or target > nums[right]:
#             right = middle -1
#         else:
#             left = middle + 1
#     return -1
    