def twoSum(numbers, target):
    hash = {}
    for i in range(len(numbers)):
        num = numbers[i]
        diff = target - num
        if diff in hash:
            return [hash[diff]+1, i+1]

        hash[num] = i



numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(numbers, target):
    left, right = 0, len(numbers)-1

    while left < right:
        currentSum = numbers[left] + numbers[right]

        if currentSum > target:
            right -= 1
        elif currentSum < target:
            left += 1
        else:
            return [left + 1, right + 1]
    return []