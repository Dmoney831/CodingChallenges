# def removeElement(nums, val):
#     for i in nums:
#         if i == val:
#             nums.remove(i)
#     print(nums)

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k



nums = [3,2,2,3] 
val = 3
removeElement(nums, val)