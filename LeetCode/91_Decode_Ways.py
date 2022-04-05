'''
Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping.
'A' -> "1"
'B' -> "2"
'Z' -> "26"

To decode an encoded messagek all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Input: s = "12"
output: 2 
Explnation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Iput: s ="06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
'''

def numDecodings(s):
    dp = [0] * (len(s)+1)
    dp[0] = 1
    print(dp)
    for i in range(1, len(dp)):
        # print(s[i])
        if int(s[i-1]) != 0:
            dp[i] = dp[i-1]
        if i != 1 and '09' < s[i-2:i] < '27':
            # print(s[i-2:i])
            # print(dp[i-2])
            dp[i] += dp[i-2]
    return dp[-1]


a = '226'
b = '111'
c = '612312'
print(numDecodings(a))
# print(numDecodings(b))
# print(numDecodings(c))

