def dailyTemperatures(temperatures):
    res = [0]*len(temperatures)
    stack = [] # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            print(stack)
            stackT, stackInd = stack.pop()
            print(stackT, stackInd)
            res[stackInd] = (i - stackInd)
            print(res, res[stackInd], i, stackInd)
        stack.append([t, i])
    return res




temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
print(dailyTemperatures(temperatures))
# time: O(n^2)