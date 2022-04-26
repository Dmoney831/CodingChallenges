var evalRPN = function(tokens) {
    var stack = [];
    for (let i in tokens) {
        if (tokens[i] == "+") {
            stack.push(stack.pop() + stack.pop())
        } else if (tokens[i] == "-") {
            let a = stack.pop()
            let b = stack.pop()
            stack.push(b - a)
        } else if (tokens[i] == "*") {
            stack.push(stack.pop() * stack.pop())
        } else if (tokens[i] == "/") {
            let a = stack.pop()
            let b = stack.pop()
            stack.push(parseInt(b/a))
        } else {
            stack.push(parseInt(tokens[i]))
        }
    }
    return stack[0]
}