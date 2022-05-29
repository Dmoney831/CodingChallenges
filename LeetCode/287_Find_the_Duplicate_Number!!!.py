def findDuplicate(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        # print(slow, fast)
    slow = 0
    print("next")
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        # print(slow, fast)
    return slow
        
def findDuplicate(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

def findDuplicate(nums):
    low = 1
    high = len(nums) - 1
    while low < high: 
        mid = low+(high-low)/2
        count = 0
        for i in nums: 
            if i <= mid:
                count += 1
        if count <= mid:
            low = mid+1
        else:
            high = mid
    return low






nums = [2,5,9,6,9,3,8,9,7,1]
# nums = [1,3,4,2,2]
print(findDuplicate(nums))