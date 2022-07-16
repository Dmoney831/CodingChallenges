
def isPalindrome(x):
    if x < 0:
        return False
    z = x
    rev = 0
    while z > 0:
        rev = (rev * 10) + (z % 10)
        z = z // 10
    return x == rev




x = 121
# output = true
print(isPalindrome(x))