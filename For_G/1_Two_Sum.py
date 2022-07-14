def twoSum(nums, target):
    hash = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hash:
            return [hash[diff], i]
        hash[n] = i
    return 


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))