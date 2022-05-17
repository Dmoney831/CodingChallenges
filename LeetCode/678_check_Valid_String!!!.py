def checkValidString(s):
    leftMin, leftMax = 0, 0
    for i in s:
        if i == "(":
            leftMin += 1
            leftMax += 1
        if i == ")":
            leftMin = max(leftMin - 1, 0)
            leftMax -= 1
        if i == "*":
            leftMin = max(leftMin - 1, 0)
            leftMax += 1
        if leftMax < 0:
            return False
        return leftMin == 0

s = "()"
# Output: true

s = "(*)"
# Output: true

s = "(*))"
# Output: true
print(checkValidString(s))