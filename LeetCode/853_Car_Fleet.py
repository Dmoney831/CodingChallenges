def carFleet(target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    print(sorted(pair)[::-1])
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) / s)
        print(stack) 
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return stack
    


target = 10
position = [3]
speed = [3]
# Output: 1

target = 100 
position = [0,2,4]  
speed = [4,2,1]
# Output: 1

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
# Output: 3
print(carFleet(target, position, speed))