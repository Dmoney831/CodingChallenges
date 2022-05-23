def longestPalindrome(s):
    result = "" 
    result_len = 0

    for i in range(len(s)):
        # odd length
        l,r = i,i
        while l >= 0 and r < len(s) and s[l]==s[r]:
            # print(f'first {l}, {r}')
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            # print(f'result: {result}')
            l -= 1
            r += 1
            # print(f'second {l}, {r}')
        # even length
        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            print(l,r)
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            l -= 1 
            r += 1
    
    return result

a = "babad"
b = "cbbe"
c = "nursesrun"
d = "abbab"
# print(longestPalindrome(a))
# print(longestPalindrome(b))
# print(longestPalindrome(c))
# print(longestPalindrome(d))

def longestPalindrome(s):
    res = ""
    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    for i in range(len(s)):
        # odd case, like "aba"
        temp = helper(s, i , i)
        if len(temp) > len(res):
            res = temp
        # even case, like "abba"
        temp = helper(s, i, i+1)
        if len(temp) > len(res):
            res = temp
    return res

print(longestPalindrome(a))    
print(longestPalindrome(c))

print(longestPalindrome(d))
