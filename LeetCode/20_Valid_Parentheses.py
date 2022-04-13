'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
'''
def isValid(s):
    stack = []
    
    table = { '(':')', '{':'}', '[':']' }
    for par in s:
        if par in table.keys():
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            z = stack.pop()
            if par != table[z]:
                return False
    return len(stack) == 0


s = "()[]{}"
print(isValid(s))