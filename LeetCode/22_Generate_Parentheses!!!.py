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


def generateParenthesis(n):
    # only add open parentheses if open < n
    # only add a closing parentheses if closed < open
    # valid IIF open == closed == n
    stack = []
    res = []
    def backtrack(openN, closedN):
        if openN == closedN == n:
            # print(res)
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            print(stack)
            backtrack(openN + 1, closedN)
            stack.pop()
            # print(stack)
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
    backtrack(0,0)
    # print(len(res))
    return res

print(generateParenthesis(3))