class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = sum(piles)
        highestK = max(piles)
        minK = (total_bananas + h - 1) // h

        l = minK
        r = highestK
        res = l
        while l <= r:
            k = (l + r) // 2

            cur_h = self.hours_needed(piles, k)
            print("l: ", l, " r: ", r, " k: ", k, " cur_h: ", cur_h)
            if cur_h <= h:
                #eating too fast, can go slower
                res = k
                r = k - 1
            else:
                #eating too slow
                l = k + 1
        return res

    def hours_needed(self, piles:List[int], k:int):
        return sum([(p + k - 1) // k for p in piles])
