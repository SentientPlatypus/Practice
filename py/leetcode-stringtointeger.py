
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        index = len(s)
        for x in range(len(s)):
            if s[x] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                if x == 0 and s[x] in ["-", "+"]:
                    continue
                index = x
                break
        s = s[:index]
        final = 0
        try:
            final = int(float(s))
            final = max(final, -2147483648)
            final = min(final, 2**31 - 1)
        except:
            pass
        return final
    
s = input()
print(Solution().myAtoi(s))