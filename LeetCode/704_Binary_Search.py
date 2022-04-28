def search(nums, target):
    nums.sort()
    print(nums)
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = ((l + r) // 2)
        print(m)
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1





nums = [-1,0,3,5,9,12] 
target = 9
nums = [5] 
target = 5

print(search(nums, target))