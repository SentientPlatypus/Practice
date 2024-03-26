class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dp = {}

        m = nums[0]
        for i in nums:
            m = max(i, m)
            dp[i] = 1
        
        for i in range(1, m + 2):
            if i not in dp:
                return i

        return 1
        