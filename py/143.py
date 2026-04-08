# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head:Optional[ListNode]):
        if not head or not head.next:
            return head
        
        rev_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = head
        f = head

        while f and f.next:
            s = s.next
            f = f.next.next
        
        #s is now the first node of our second linked list
        #merge the linked lists starting at head and s respectively
        l1 = head
        l2 = self.reverseList(s.next)
        s.next = None        


        while l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2
        return l1







        
