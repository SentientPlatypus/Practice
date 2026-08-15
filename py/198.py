class Solution:

    def robOpt(self, nums:List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        b4b4 = nums[0]
        b4 = max(nums[0], nums[1])
        cur = 0

        for i in range(2, len(nums)):
            cur = max(b4b4 + nums[i], b4)

            b4b4 = b4
            b4 = cur
        
        return b4


    def robTab(self, nums: List[int]) -> int:
        N = len(nums)

        if N <= 1:
            return nums[0]

        dp = [0 for _ in range(N)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[N - 1]

    
    def rob(self, nums:List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]


        memo = {}

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        def M(i):
            if i in memo:
                return memo[i]
            
            memo[i] = max(M(i - 1), M(i - 2) + nums[i])
            return memo[i]
        
        return M(len(nums) - 1)


    
    
