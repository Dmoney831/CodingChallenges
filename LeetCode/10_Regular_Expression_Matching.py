def isMatch(s,p):
    if len(s) != len(p):
        return False
    prev = ""
    arr = []
    for i in range(len(s)):
        print(i)
        if p[i] == ".":
            p[i] == s[i]
        elif p[i] == "*":
            p[i] == prev
        elif p[i] != s[i]:
            return False
        prev = p[i]
    return True

def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])


def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


def isMatch(text, pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

s, p = "aa", "a"
s, p = "aa", "a*"
s, p = "ab", ".*"
s, p = "aab", "c*a*b"

print(isMatch(s,p))
