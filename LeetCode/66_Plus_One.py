def plusOne(digits):
    d = ""
    for i in digits:
        d += str(i)
    d = int(d) + 1
    ans = [int(j) for j in str(d) ]
    return ans
    



digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].


digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].


# digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


# ********Time Complexity: O(n)
# ********Space Complexity: O(n)

def plusOne(digits):
    x = int("".join([str(n) for n in digits]))
    y = x + 1
    z = [int(i) for i in str(y)]
    return z

    
print(plusOne(digits))