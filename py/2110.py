class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = 0
        res = 1
        for r in range(1, len(prices)):
            if prices[r - 1] == prices[r] + 1:
                res += (r - l + 1)
            else:
                l = r
                res += 1
        return res
