import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        print(nums)
        n = 0
        d = 1


        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            n = n * den + num * d
            d *= den
        
        common_divisor = Solution.gcd(n, d)
        return f"{n // common_divisor}/{d // common_divisor}"
    
    def gcd(a, b):
        if b == 0:
            return a
        return Solution.gcd(b, a % b)