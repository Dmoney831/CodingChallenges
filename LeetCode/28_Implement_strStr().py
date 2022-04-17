def strStr(haystack, needle):
    if haystack is None or needle is None:
        return -1
    if haystack == needle:
        return 0
    z = len(needle)
    for i in range(len(haystack) +1 - z):
        if haystack[i: i + z] == needle:
            return i
    return -1

    
haystack = "hello" 
needle = "ll"
print(strStr(haystack, needle))
print(haystack[2:4])