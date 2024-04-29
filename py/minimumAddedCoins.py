class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        m = 1
        a = 0
        i = 0

        while m <= target:
            if i < len(coins) and coins[i] <= m:
                m += coins[i]
                i += 1
            else:
                m += m
                a += 1
        
        return a