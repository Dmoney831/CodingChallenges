# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
# this solution above is recurisve function.
# Time Complexity: O(n), linear
# Space Complexity: O(n), 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev, cur):
            if not cur:
                return prev
            tail = rec(cur, cur.next)
            cur.next = prev
            return tail
        return rec(None, head)

######### Optimal Solution #######
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

# This solution above is optimal solution.
# time complexity: O(n)
# space complexity: O(1)