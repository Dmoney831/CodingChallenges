class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""
        while head:
            res += str(head.val)
            head = head.next
        to_decimal = int(res, 2)
        return to_decimal