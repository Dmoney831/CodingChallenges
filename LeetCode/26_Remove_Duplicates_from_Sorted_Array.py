def removeDuplicates(nums):
    length = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[length] = nums[i]
            length += 1
    return length
