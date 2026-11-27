class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i - 1 for i in range(n + 1)]



        for i in range(1, n + 1):
            for j in range(1, i): #everything before i is optimal already
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        
        return dp[n]
