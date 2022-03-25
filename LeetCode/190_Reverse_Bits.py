def reverseBits(n):
    ans = 0
    for i in range(32):
        bit = (n >> i) & 1
        ans = ans | (bit << (31 - i))
        print(bit)
    print(ans)
    # return ans
    




reverseBits(0b10100101000001111010011100)
# print("{0:#b}".format(2))