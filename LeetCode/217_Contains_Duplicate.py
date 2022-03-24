def containsDuplicate(nums):
    x = set(nums)
    if len(set(nums)) < len(nums):
        return True
    else:
        return False

    

# a = [1,2,3,1]
# a = [1,2,3,4]
# a = [1,1,1,3,3,4,3,2,4,2]

# print(containsDuplicate(a))