def trap(height):
    # iterate through the array and use dp to record the prev max value - current value
    area = 0
    max_l = max_r = 0
    l = 0
    r = len(height) - 1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                area += max_l - height[l]
            l += 1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                area += max_r - height[r]
            r -= 1
    return area



height = [0,1,0,2,1,0,1,3,2,1,2,1] #output = 6
height = [4,2,0,3,2,5] #output = 9

print(trap(height))