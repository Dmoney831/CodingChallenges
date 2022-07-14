def longestCommonPrefix(strs):
    z = len(strs)
    min_len = min(len(strs[0]), len(strs[z-1]))
    left = 0
    while (left < min_len) and (strs[0][left] == strs[z-1][left]):
        left += 1
    prefix = strs[0][:left]
    return prefix



strs = ["flower", "flow", "flight"]
# output = "fl"
# strs = ["dog","racecar","car"]

print(longestCommonPrefix(strs))