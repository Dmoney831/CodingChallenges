def findDuplicate(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        print(slow, fast)
    slow = 0
    print("next")
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        print(slow, fast)
    return slow
        
    # return nums[slow]




nums = [2,5,9,6,9,3,8,9,7,1]
# nums = [1,3,4,2,2]
print(findDuplicate(nums))