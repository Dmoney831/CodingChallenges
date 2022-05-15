def jump(nums):
    jump = curEnd = curFar = 0
    end = len(nums) 
    for i in range(end - 1):
        curFar = max(curFar, i + nums[i])
        if curEnd == i:
            jump += 1
            curEnd = curFar
    return jump

def jump(nums):
    count = 0
    reach = 0
    landing = 0
    for idx, num in enumerate(nums):
        reach = max(reach, idx + num)
        # print(f'reach: {reach}, idx: {idx}, num: {num}, landing: {landing}, count: {count}')
        if landing == idx:
            count += 1
            landing = reach
    return count - 1





nums = [2,3,1,1,4]
# Output: 2
# nums = [2,3,0,1,4]
# Output: 2
nums = [2,3,1,4,2,1,1,1,3,2,1,1,1,1,1,1]

print(jump(nums))