class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x : len(x))

        dp = {}
        for w in words:
            dp[w] = 1 #longest chain ending with w.


        for w in words:
            predecessors = []
            for i in range(len(w)):
                predecessor = w[:i] + w[min(len(w), i + 1):]
                if predecessor in dp.keys():
                    dp[w] = max(dp[w], dp[predecessor] + 1)

        
        
        return max(v for k,v in dp.items())
