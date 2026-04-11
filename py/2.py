# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2

        res = ListNode(0)
        cur = res
        carry = 0
        while c1 and c2:
            newsum = c1.val + c2.val + carry
            newNode = ListNode(newsum % 10)

            if newsum > 9:
                carry = 1
            else:
                carry = 0

            cur.next = newNode
            cur = cur.next

            c1 = c1.next
            c2 = c2.next
        

        rest = c1 if c1 else c2

        while rest:
            newsum = rest.val + carry
            newNode = ListNode(newsum % 10)

            if newsum > 9:
                carry = 1
            else:
                carry = 0
            
            cur.next = newNode

            cur = cur.next
            rest = rest.next

        if carry:
            cur.next = ListNode(carry)

        return res.next
