# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortoise = head
        hare = head

        while tortoise.next and hare.next:
            tortoise = tortoise.next
            hare = hare.next

            if hare.next:
                hare = hare.next
            else:
                return False
            
            if tortoise == hare:
                return True
        
        if not hare.next:
            return False

        
