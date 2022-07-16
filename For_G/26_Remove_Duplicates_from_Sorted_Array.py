def removeDuplicates(nums):
    length = 1
    for i in range(len(nums)):
        if i > 0 and nums[i-1] != nums[i]:
            nums[length] = nums[i]
            length += 1
        return length