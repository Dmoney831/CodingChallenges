def mySqrt(x):
    if x <= 1:
        return x
    for i in range(1, x+1):
        if i * i == x:
            return i
        if i * i > x:
            return i - 1
        
def mySqrt(x):
    if x == 1:
        return 1
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid+1) * (mid+1):
            return mid
        elif mid * mid < x:
            left = mid
        elif mid * mid > x:
            right = mid

x = 4
# output: 2

x = 8
# output: 2 // The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned. 

x = 2
x = 3


print(mySqrt(x))