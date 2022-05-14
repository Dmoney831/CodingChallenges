import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Input: ["KthLargest", "add", "add", "add", "add", "add"]
#        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output: [null, 4, 5, 5, 8, 8]