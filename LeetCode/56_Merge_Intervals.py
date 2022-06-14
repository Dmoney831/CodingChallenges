def merge(intervals):
    intervals.sort(key = lambda x: x[0])
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

# Time Complexity: In python, use sort method to a list costs O(n log n), where n is the length of the list. 
# the for-loop used to merge intervals, costs O(n).
# O(nlogn) + O(n) = O(nlogn)
# so the time complexity is O(nlogn)

# Space complexity: 
# The algorithm used a merged list and a variable i.
# In the worst case, the merged list is equal to the length of the input intervals list. So the space complexity is O(n), where n is the length of the input list. 
