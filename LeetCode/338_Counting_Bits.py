def countBits0(n):
    x = bin(n)
    y = "{0:b}".format(n)

    
    return [x,y]
# print(countBits0(2))

def countBits(n):
    dp = [0]*(n+1)
    print(dp)
    offset = 1
    for i in range(1, n+1):
        if offset*2 == i:
            offset = i
        dp[i] = 1+dp[i-offset]
    print(dp)


countBits(8)

def countbits1(n):
    ans = []
    for i in range(1,n+1):
        if i % 2 != 0:
            i = 1+





print(countbits1(n))
print(11 // 2)