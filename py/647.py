class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)

        dp = [[False] * N for _ in range(N)]
        res = 0

        for length in range(1, N + 1):
            for i in range(N - length + 1):
                j = i + length - 1

                if s[i] == s[j]:
                    if length <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        
        return res

        
                
