# def maxArea(height):
#     max_area = 0
#     for h1 in range(len(height)-1):
#         for h2 in range(h1, len(height)):
#             area = min(height[h1], height[h2]) * (h2 - h1)
#             max_area = max(area, max_area)
#     print(max_area)

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




a = [1,8,6,2,5,4,8,3,7]
b = [1,1]
c = [2,3,4,5,18,17,6]

print(maxArea(c))