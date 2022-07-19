def plusOne(digits):
    x = ""
    for n in digits:
        x += str(n)    
    y = int(x) + 1
    ans = [int(z) for z in str(y)]
    return ans

digits = [1,2,3]
# output: [1,2,4]

digits = [4,3,2,1]
# output: [4,3,2,2]

print(plusOne(digits))