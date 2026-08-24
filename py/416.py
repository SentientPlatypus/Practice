class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        N = len(nums)
        TOTAL = sum(nums)

        if TOTAL % 2 != 0:
            return False

        TARGET = TOTAL // 2

        def M(i, xsum):
            if xsum == TARGET:
                return True
            elif xsum >= TARGET:
                return False

            if i >= N:
                return xsum == TARGET

            if (i, xsum) in memo:
                return memo[(i, xsum)]
            
            memo[(i, xsum)] = M(i + 1, xsum + nums[i]) or M(i + 1, xsum)
            return memo[(i, xsum)]
        
        return M(0, 0)
        
