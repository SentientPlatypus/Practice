class Solution:
    def reverse(self, n:int):
        if n < 10:
            return n
        return (n % 10) * (10 ** (len(str(n)) - 1)) + self.reverse(n // 10)

    def mirrorDistance(self, n: int) -> int:
        return abs(self.reverse(n) - n)
