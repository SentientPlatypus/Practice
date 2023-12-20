class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        l = 1000
        sl = 999

        for p in prices:
            if p < l:
                sl = l
                l = p
            elif p < sl:
                sl = p

        return money - l - sl if money - l - sl >=0 else money
        