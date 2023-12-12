class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h = 0
        secondh = 0

        for i in nums:
            if i > h:
                secondh = h
                h = i
            elif i > secondh:
                secondh = i
        
        return (h-1) * (secondh-1)