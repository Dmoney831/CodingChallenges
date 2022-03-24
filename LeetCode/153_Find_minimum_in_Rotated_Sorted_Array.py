def findMin(nums):
    left = 0
    right = len(nums)-1

    while left < right:
        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    return nums[left]
    
# def findMin(nums):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         middle = (left + right) // 2
#         if nums[middle] > nums[right]:
#             left = middle + 1
#         else:
#             right = middle
#     return nums[left]


a = [3,4,5,1,2]
b = [4,5,6,7,0,1,2]
c = [11,13,15,17]

print(findMin(b))