def isValid(s):
    stack = []
    table = { "(": ")", "{": "}", "[": "]" }
    for par in s:
        if par in table:
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            z = stack.pop()
            if table[z] != par:
                return False
    return len(stack) == 0

# s = "()"
s = "()[]{}"
# s = "(]"
print(isValid(s))