def isPalindrome(x):
    if x < 0:
        return False
    
    z = x
    rev = 0
    while x > 0:
        rev = rev*10 + (x%10)
        x = int(x/10)
    return z == rev




x = 121
x = 123454321
x = -123454321
# Output: true
print(isPalindrome(x))