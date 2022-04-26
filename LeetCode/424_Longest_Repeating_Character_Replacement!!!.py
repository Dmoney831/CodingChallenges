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


s = "ABAB"
k = 2
print(characterReplacement(s, k))