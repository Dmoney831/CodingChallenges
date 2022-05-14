import collections
def leastInterval(tasks, n):
    count = [value for value in collections.Counter(tasks).values()]
    count.sort()
    max_freq = count.pop()
    room = max_freq - 1
    idle = (room) * n
    print(count, room, idle)
    while count and idle > 0:
        idle -= min(room, count.pop())
        print(f'idle: {idle}')
    print(count)
    return max(0, idle) + len(tasks)

tasks = ["A","A","A","B","B","B"] 
n = 2
# Output: 8
tasks = ["A","A","A","B","B","B"] 
n = 0
# Output: 6
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
# Output: 16

print(leastInterval(tasks, n))
# *****Time Complexity: O(n)*******
# *****