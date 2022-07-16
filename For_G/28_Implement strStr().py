def strStr(haystack, needle):
    if haystack == needle:
        return 0
    z = len(needle)
    for i in range(len(haystack) - z + 1):
        if haystack[i:i+z] == needle:
            return i
    return -1

haystack = "aaaaa"
needle = "bba"
# output: -1

haystack = "hello"
needle = "ll"
# output: 2

print(strStr(haystack, needle))