class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        memo[0] = 0
        memo[1] = 0
    
        def M(i:int) -> int:
            if i in memo:
                return memo[i]
            
            memo[i] = min(M(i - 1) + cost[i - 1], M(i - 2) + cost[i - 2])
            return memo[i]
        
        return M(len(cost))


            


