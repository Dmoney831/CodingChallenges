def canCompleteCircuit(gas, cost):
    length = len(gas)
    start = 0
    current = 0 
    tank = 0
    for i in range(length):
        t = gas[i] - cost[i]
        tank += t
        current += t
        if current < 0:
            current = 0
            start = i + 1
    return -1 if tank < 0 else start
        

gas = [1,2,3,4,5] 
cost = [3,4,5,1,2]
# Output: 3
gas = [2,3,4] 
cost = [3,4,3]
# Output: -1

print(canCompleteCircuit(gas, cost))
# *******Time Complexity: O(n)
# *******Space Complexity: O(1)