class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #invariant: nums1 is <= to nums2 length wise
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = 0
        r = len(nums1)
        i = 0
        j = 0

        while l <= r:
            #the invariant we want to hold is that left side of nums1 must be smaller than right side of nums2
            #additionally, partition i, j such that i + j = (m + n) / 2.

            i = (l + r) // 2
            j = (len(nums1) + len(nums2)) // 2 - i

            leftA = nums1[i-1] if i > 0 else float('-inf')
            rightA = nums1[i] if i < len(nums1) else float('inf')

            leftB = nums2[j-1] if j > 0 else float('-inf')
            rightB = nums2[j] if j < len(nums2) else float('inf')

            if leftA > rightB:
                r = i - 1
            elif rightA < leftB:
                l = i + 1
            if leftA <= rightB and leftB <= rightA:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
