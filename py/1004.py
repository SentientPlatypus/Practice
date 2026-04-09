class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0

        nz = 0
        for r in range(len(nums)):
            nxt = nums[r]

            if nxt == 0:
                nz += 1
            
            if nz <= k:
                res = max(res, r - l + 1)
            else:
                if nums[l] == 0:
                    nz -= 1
                l += 1
        
        return res
            
