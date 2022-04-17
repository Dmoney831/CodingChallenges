def removeDuplicates(nums):
    length = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[length] = nums[i]
            length += 1
    return length

'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
'''