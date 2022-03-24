def hammingWeight(n):
    ans = 0
    while n:
        ans += n % 2
        n = n >> 1
    return ans



# a = 00000000000000000000000000001011
# b = 00000000000000000000000010000000
# c = 11111111111111111111111111111101

# hammingWeight(a)
# print(hammingWeight(c))
# hammingWeight(c)



