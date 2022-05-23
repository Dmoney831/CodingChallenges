
def maxArea(height):
    left = 0
    right = len(height) -1
    ans = 0
    while left < right:
        a = min(height[left], height[right]) * (right - left)
        ans = max(a, ans)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans

# area = base * height
def maxArea(height):
    left = 0
    right = len(height) - 1
    answer = 0
    while left < right:
        area = min(height[left] * height[right] * (right - left))
        answer = max(answer, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return answer




a = [1,8,6,2,5,4,8,3,7]
b = [1,1]
c = [2,3,4,5,18,17,6]

print(maxArea(c))