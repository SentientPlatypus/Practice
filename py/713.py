class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        res = 0
        l = 0
        curProd = 1
        for r in range(len(nums)):
            curProd *= nums[r]

            if curProd < k:
                res += (r - l + 1)
            else:
                while l < len(nums) and curProd >= k:
                    curProd /= nums[l]
                    l += 1
                res += (r - l + 1)
        
        return res
