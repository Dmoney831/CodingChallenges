def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1


n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
print(isHappy(n))

# *********Time Complexity: O(n)
# *********Space Complexity: O(n) since we use set() and store number of n