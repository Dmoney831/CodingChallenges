'''
Write a function to find the longest common prefix string amongst an array of strings.

Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
'''

def longestCommonPrefix(strs):
    strs.sort()
    z = len(strs)
    min_len = min(len(strs[0]), len(strs[z-1]))

    l = 0
    while l < min_len and strs[0][l] == strs[z-1][l]:
        l += 1
    prefix = strs[0][:l]
    print(prefix)

    # print(strs)
    # print(min_len)






strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]

longestCommonPrefix(strs)