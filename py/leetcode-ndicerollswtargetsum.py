class Solution:
    self.m = 10 ** 9 + 7
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)
    
    def recursion(self, dp:list, n:int, k:int, target:int) -> int:
        if target == 0 and n == 0:
            return 1
        
        if n == 0 or target <=0:
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target] % self.m
        
        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i) % self.m)
        dp[n][target] = ways % self.m
        return dp[n][target]