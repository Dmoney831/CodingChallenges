class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

head = [1,2,3,4,5]
# Output: [3,4,5]


head = [1,2,3,4,5,6]
# Output: [4,5,6]
