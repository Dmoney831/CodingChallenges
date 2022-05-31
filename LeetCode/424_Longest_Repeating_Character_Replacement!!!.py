# Time Complexity: O(26*n) => O(n)

def characterReplacement(s, k):
    count = {}
    result = 0

    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        # print(count)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        print(max(count.values()))
        print(count)
        result = max(result, r - l + 1)

    return result

def characterReplacement(s,k):
    count = {}
    length = 0
    left = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)

        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
        
        length = max(length, (right - left + 1))
    return length

s = "ABAB"
k = 2
print(characterReplacement(s, k))