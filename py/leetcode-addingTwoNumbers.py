# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getNormalList(l:ListNode):
        final = []
        while l:
            final.append(l.val)
            l = l.next
        return final

    def getNumFromNormalList(l):
        f = 0
        powers = list(range(len(l)))

        for value, power in zip(l, powers):
            f += value * 10**power
        return f

    def getListFromN(n):
        if n // 10 == 0:
            return ListNode(val = n)
        
        return ListNode(val = n % 10, next = Solution.getListFromN(n // 10))
    
        

            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = Solution.getNumFromNormalList(Solution.getNormalList(l1))
        v2 = Solution.getNumFromNormalList(Solution.getNormalList(l2))
        return Solution.getListFromN(v1 + v2)


