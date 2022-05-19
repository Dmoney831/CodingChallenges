class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step 1: find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        second = slow.next
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        slow.next = None
        
        # step 3: merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# Time Complexity is O(n), because we first do O(n) iterations to find middle, then we do O(n) iterations to reverse second half and finally we do O(n) iterations to merge lists.
# Space complexity is O(1).
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # step1 find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # step2 reverse the second half
        second = slow.next
        prev = None 
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        slow.next = None
        # step3 merge two lists

        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first = nxt1 
            second = nxt2
            


        
