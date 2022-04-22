class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"

# print(Solution.lengthOfLongestSubstring(self, "abcabcbb" ))

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            print(charSet, s[r], s[l], l)
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

# def lengthOfLongestSubstring(s):
#     sSet = set(s)
#     return sSet

print(lengthOfLongestSubstring(s))