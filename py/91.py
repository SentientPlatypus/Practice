class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        if not s or s[0] == "0":
            return 0

        dp = [0] * (N + 1)
        dp[1] = 1
        dp[0] = 1

        for i in range(2, N + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[N]


                
