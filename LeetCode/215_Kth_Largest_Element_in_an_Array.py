import heapq
def findKthLargest(nums, k):
    heapq.heapify(nums)
    # print(nums)
    length = len(nums)
    while len(nums) > k:
        heapq.heappop(nums)
        length -= 1            
    return nums[0]

def findKthLargest(nums, k):
    # heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]

def findKthLargest(nums, k):
    heapq.heapify(nums)
    length = len(nums)
    while length > k:
        heapq.heappop(nums)
        length -= 1
    return nums[0]

nums = [3,2,1,5,6,4] 
k = 2
# Output: 5

# nums = [3,2,3,1,2,4,5,5,6] 
# k = 4
# Output: 4

# nums = [2,1]
# k = 1
print(findKthLargest(nums, k))
# ********Time Complexity: O(nlogn)