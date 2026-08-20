class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N1 = len(word1)
        N2 = len(word2)
        dp  = [[9999 for _ in range(N2 + 1)] for _ in range(N1 + 1)]
        print(dp)

        #dp[i][j] = number of edits needed to turn word1[:i] into word2[:j]


        #base cases
        for i in range(N1 + 1):
            dp[i][0] = i
        
        for j in range(N2 + 1):
            dp[0][j] = j

        for i in range(1, N1 + 1):
            for j in range(1, N2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        
        return dp[N1][N2]


        
