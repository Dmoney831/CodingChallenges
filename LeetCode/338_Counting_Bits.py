def countBits0(n):
    x = bin(n)
    y = "{0:b}".format(n)

    
    return [x,y]
# print(countBits0(2))

def countBits(n):
    dp = [0]*(n+1)
    # print(dp)
    offset = 1
    for i in range(1, n+1):
        if offset*2 == i:
            offset = i
        dp[i] = 1+dp[i-offset]
    return dp


# countBits(8)

def countbits1(n):
    ans = [0]
    for i in range(1,n+1):
        ans.append(ans[i & (i-1)] + 1)
    return ans



print(countbits1(8))
# print(1 // 2)

def whatisnpercent(n):
    for i in range(1, n+1):
        print(i & (i-1)+1)

whatisnpercent(5)