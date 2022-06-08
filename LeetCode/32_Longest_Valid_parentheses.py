def longestValidParentheses(s):
    dp = [0] * (len(s) + 1)
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
            print(stack)
        else:
            if stack:
                p = stack.pop()
                print(F"p: {p}, i: {i}, dp[p]: {dp[p]}")
                dp[i+1] = dp[p] + i - p + 1
                print(dp)
    return max(dp)


s = "(()"
# output -> 2
s = ")()())"
# output -> 4
# s = ''
# output = 0
s = "()(())"
# s = ")()())"


print(longestValidParentheses(s))