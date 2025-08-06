class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        l = 0
        cur = 0
        res = 0

        for r in range(len(fruits)):
            cur += fruits[r][1]

            while l <= r and  min(abs(startPos - fruits[l][0]) + fruits[r][0] - fruits[l][0], abs(startPos - fruits[r][0]) + fruits[r][0] - fruits[l][0]) > k:
                cur -= fruits[l][1]
                l+=1

            res = max(res,cur)
        return res