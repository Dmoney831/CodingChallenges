def insert(intervals, newInterval):
    res = []

    for interval in intervals:
        if interval[1] < newInterval[0]:
            res.append(interval)
        elif interval[0] > newInterval[1]:
            res.append(newInterval)
            newInterval = interval
        elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
    res.append(newInterval)
    return res

intervals = [[1,3],[6,9]] 
newInterval = [2,5]
# Output: [[1,5],[6,9]]


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]] 
newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

print(insert(intervals, newInterval))