# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #basecase: we dont have enough nodes
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        #we have enough
        prev = None
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
        
        if cur:
            head.next = self.reverseKGroup(cur, k)
        return prev
        
