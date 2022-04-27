
def generateParenthesis(n):
    res = []

    def dfs(l, r, temp):
        if not l and not r:
            res.append(temp[:])
            print(res)
        if l:
            dfs(l - 1, r, temp + "(")
        if l < r:
            dfs(l, r - 1, temp + ")")
    dfs(n, n, "")
    # return res
    print(res)





generateParenthesis(2)