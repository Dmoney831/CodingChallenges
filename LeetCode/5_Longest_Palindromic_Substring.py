def longestPalindrome(s):
    result = "" 
    result_len = 0

    for i in range(len(s)):
        # odd length
        l,r = i,i
        while l >= 0 and r < len(s) and s[l]==s[r]:
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            l -= 1
            r += 1
        # even length
        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > result_len:
                result = s[l:r+1]
                result_len = r - l + 1
            l -= 1 
            r += 1
    
    return result

a = "babad"
b = "cbbe"
c = "nursesrun"
print(longestPalindrome(a))
print(longestPalindrome(b))
print(longestPalindrome(c))

# def longestPalindrome(s):
#     result = ""
#     result_len = 0
#     for i in range(len(s)):
#         l,r = i,i
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > result_len:
#                 result = s[l:r+1]
#                 result_len = r - l + 1
#             l -= 1
#             r += 1

#         l,r = i, i+1
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             if (r - l + 1) > result_len:
#                 result = s[l:r+1]
#                 result_len = r - l + 1
#             l -= 1
#             r += 1
#     return result, result_len


# a = "babad"
# b = "cbbe"
# c = "nursesrun"
# print(longestPalindrome(a))
# print(longestPalindrome(b))
# print(longestPalindrome(c))
