def merge(intervals):
    # intervals.sort(key = lambda x: x[1])
    print(intervals)
    arr = []
    for i in intervals:
        if not arr or arr[-1][-1] < i[0]:
            arr.append(i)
        else:
            arr[-1][-1] = max(arr[-1][-1], i[-1])
    return arr

intervals = [[1,3],[2,6],[8,10],[15,18]] # output: [[1, 6], [8, 10], [15, 18]]

# intervals = [[1,4],[4,5]] # output: [[1, 5]]

print(merge(intervals))

# Time Complexity: 