# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count = 1
        l = head
        while 1:
            count += 1
            l = l.next
            if not l:
                break
        print("count = ", count)



        i = 0
        vals = {}
        maxval = -1
        while 1:
            print(head.val)
            try:
                maxval = max(vals[i + 1] + head.val, maxval)
            except:
                vals[count - 1 - i] = head.val
            head = head.next
            i += 1
            if not head:
                break

        print(vals)
        return maxval