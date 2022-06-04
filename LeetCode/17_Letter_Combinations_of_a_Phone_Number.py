from collections import deque
def letterCombinations(digits):
    d = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "prs", "8": "tuv", "9": "wxyz"}
    q = deque(d[(digits[0])])
    print(q)
    print(len(digits))
    for i in range(1, len(digits)):
        s = len(q)
        while s:
            out = q.popleft()
            for j in d[digits[i]]:
                q.append(out + j)
            s -= 1
    return q

    




digits = "23"
output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# digits = ""
output = []
# digits = "2"
output = ["a", "b", "c"]

print(letterCombinations(digits))