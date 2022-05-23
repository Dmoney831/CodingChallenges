def isPalindrome(x):
    if x < 0:
        return False
    
    z = x
    rev = 0
    while x > 0:
        rev = rev*10 + (x%10)
        x = int(x/10)
    return z == rev



def isPalindrome(x):
    if x < 0:
        return False
    z = x 
    rev = 0
    while z > 0:
        rev = rev*10 + (z%10)
        z = z//10
    print(x, rev, z)
    return x == rev
x = 121
x = 123454321
# x = -123454321
# Output: true
print(isPalindrome(x))