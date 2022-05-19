def hasCycle(self, head: ListNode) -> bool:
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            return True
    return False


# Time Complexity: O(m+n) where ms steps of fast pointer and n is steps of slow pointer.
# Space Complexity: O(1)