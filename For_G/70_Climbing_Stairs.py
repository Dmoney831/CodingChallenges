def climbStairs(n):
    x = y = 1
    for _ in range(n):
        x, y = y, x+y
        print(x, y)
    return x

n = 2
# output: 2

n = 3
# output: 3

print(climbStairs(n))