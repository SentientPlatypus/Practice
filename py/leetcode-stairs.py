class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        return self.fib(n, dp)
    
    def fib(self, n: int, dp: list) -> int:
        if n <= 3:
            return n
        if dp[n] != 0:
            return dp[n]
        dp[n] = self.fib(n - 1, dp) + self.fib(n - 2, dp)
        return dp[n]
