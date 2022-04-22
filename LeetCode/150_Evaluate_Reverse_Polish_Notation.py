def evalRPN(tokens):
    stack = []
    for ops in tokens:
        if ops == "+":
            stack.append(stack.pop() + stack.pop())
        elif ops == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif ops == "*": 
            stack.append(stack.pop() * stack.pop())
        elif ops == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(ops))
    
    return stack[0]



tokens = ["2","1","+","3","*"]
Output = 9
tokens = ["4","13","5","/","+"]
Outpu = 6

evalRPN(tokens)

# Time Complexity: O(n)
# 