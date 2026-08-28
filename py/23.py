# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists:List[Optional[ListNode]]) -> Optional[ListNode]:
        minhp = []
        res = ListNode()
        cur = res

        for i, listhd in enumerate(lists):
            if listhd:
                heappush(minhp, (listhd.val, i))
        

        while minhp:
            minHdVal, minHdListI = heappop(minhp)
            minHd = lists[minHdListI]

            lists[minHdListI] = minHd.next

            if minHd.next:
                heappush(minhp, (minHd.next.val, minHdListI))
            
            #append to end of res
            cur.next = minHd
            cur = cur.next

        return res.next


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return res.next

    def mergeKListOld(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(-9999999999)

        for l in lists:
            res = self.mergeTwoLists(res, l)
        return res.next
        
