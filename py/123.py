class Solution:
    def maxProfit(self, prices:List[int]) ->int:
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -float("inf")
        sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)
            sell1 = max(sell1, p + buy1)
            buy2 = max(buy2, sell1 - p)
            sell2 = max(sell2, p + buy2)
        return sell2


    def maxProfitSubOptimal(self, prices: List[int]) -> int:
        N = len(prices)
        memo = {}

        def M(i, transRemaining, holding):
            if i == N or transRemaining == 0:
                return 0
            
            state = (i, transRemaining, holding)
            if state in memo:
                return memo[state]
            
            skip = M(i + 1, transRemaining, holding)

            if holding:
                act = prices[i] + M(i + 1, transRemaining - 1, False)
            else:
                act = -prices[i] + M(i + 1, transRemaining, True)
            
            memo[state] = max(skip, act)
            return memo[state]
        
        return M(0, 2, False)
            
