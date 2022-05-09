class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next



# def addTwoNumbers(l1, l2):
#     x = []
#     y = []
#     answer = []
#     for i in l1:
#         x.append(str(i))
#     for j in l2:
#         y.append(str(j))
#     num1 = "".join(x)
#     num2 = "".join(y)
#     # print(num1, num2)
#     new_num = int(num1) + int(num2)
#     # print(new_num)
#     rev_num = str(new_num)[::-1]
#     # print(rev_num)
#     for char in rev_num:
#         answer.append(int(char))
#     # print(answer)
#     return answer
    

# a = [2,4,3] 
# b = [5,6,4]
# c = [9,9,9,9,9,9,9] 
# d = [9,9,9,9]
# e = [0]
# f = [0]

# print(addTwoNumbers(a,b))
# print(addTwoNumbers(c,d))
# print(addTwoNumbers(e,f))

# def addTwoNumbers(l1, l2):
#     x = []
#     y = []
#     answer = []
#     for i in l1:
#         x.append(str(i))
#     for j in l2:
#         y.append(str(j))
#     num1 = "".join(x)
#     num2 = "".join(y)
#     new_num = int(num1) + int(num2)
#     rev_num = str(new_num)[::-1]
#     for char in rev_num:
#         answer.append(char)
#     return answer
