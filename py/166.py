class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if n == 0:
            return "0"
        
        sign = "-" if str((numerator * denominator) / abs(numerator * denominator)) < 0 else ""
        n, d = abs(numerator), abs(denominator)
        integerPart = n // d
        remainder = n % d

        res = [sign + str(integerPart)]

        prev_rmdrs = {}
        while remainder != 0:
            if remainder in prev_rmdrs:
                i = prev_rmdrs[remainder]
                res.insert(i, "(")
                res.append(")")
                break

            prev_rmdrs[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // d))
            remainder = remainder % d

        return "".join(res)