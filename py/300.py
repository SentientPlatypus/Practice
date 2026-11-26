class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        N = len(nums)

        dp = [1 for _ in range(N)] #dp[i] is the longest subsequence ending at index i (includingi i)

        for i in range(N):
            for j in range(i + 1, N):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], 1 + dp[i])

        return max(dp)
