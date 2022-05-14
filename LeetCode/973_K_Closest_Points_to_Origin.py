from cmath import sqrt
import heapq
def kClosest(points, k):
    heap = []
    for x,y in points:
        if len(heap)<k:
            print(heap)
            heapq.heappush(heap,[-(x*x+y*y),[x,y]])
            print(heap)
        else:
            heapq.heappushpop(heap,[-(x*x+y*y),[x,y]])
            # print(heap)
    return [pair for value, pair in heap]
    

# ****** Time Complexity: O(nlogn) where n is the size of input.

points = [[1,3],[-2,2]] 
k = 1
# Output: [[-2,2]]

points = [[3,3],[5,-1],[-2,4]] 
k = 2
# Output: [[3,3],[-2,4]]
print(kClosest(points, k))