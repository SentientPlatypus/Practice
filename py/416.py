class Solution:

    def canPartition(self, nums:List[int]) ->bool:
        N = len(nums)
        TOTAL = sum(nums)
        if TOTAL % 2 != 0:
            return False
        
        TARGET = TOTAL // 2

        dp = [[False] * (TARGET + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            dp[i][0] = True
        
        for i in range(1, N + 1):
            for j in range(1, TARGET + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

            if dp[i][TARGET]:
                return True
        
        return dp[N][TARGET]


    def canPartitionMemo(self, nums: List[int]) -> bool:
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
        
