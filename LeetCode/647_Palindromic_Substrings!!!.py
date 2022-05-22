def countSubstrings(s):
    res = 0
    l = len(s)
    for mid in range(l * 2 - 1):
        left = mid // 2
        right = left + mid % 2
        print(mid, left, right)
        while left >= 0 and right < l and s[left] == s[right]:
            print(f'left: {left}, right: {right}')
            res += 1
            left -= 1
            right += 1
    return res



def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res

def countSubstrings(self, s: str) -> int:
        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1): #each possible length when the string length is l
            for start in range(N - l + 1): #outer
                end = start+l-1
                if l == 1 or (l == 2 and s[start] == s[end]) or (l >= 3 and s[start] == s[end] and dp[start + 1][end - 1]):#dp
                    dp[start][end] = True
                    count += 1
        return count



s = "abc"
# Output: 3
# s = "aaa"
# Output: 6
s = "aba"
def countSubstrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    # print(dp)
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # print(i,j)
            if s[i] == s[j]:
                if i+1 >= j:
                    dp[i][j] = True
                    # print(f'i: {i}, j: {j}, dp[i][j]: {dp[i][j]}')
                else:
                    dp[i][j] = dp[i+1][j-1]
                    print(i,j)
            if dp[i][j]:
                ans += 1
    return ans
            

print(countSubstrings(s))