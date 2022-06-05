# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

lists = [[1,4,5], [1,3,4], [2,6]]
lists = []
lists = [[]]

# Time Complexity: O(N log N) where N is the total number of nodes. 
    # Collecting all the values costs O(N) time.
    # A stable sorting algorithm costs O(N log N) time.
    # Iterating for creating the linked list costs O(N) time.
# Space complexity: O(N)
