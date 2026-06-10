class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(starti, remainingDots, curstr):
            if starti == len(s) and remainingDots == 0:
                res.append(curstr[:-1])
                return
            
            if remainingDots:
                for endi in range(starti, min(starti + 3, len(s))):
                    segment = s[starti:endi + 1]

                    if len(segment) > 1 and segment[0] == "0":
                        break

                    if int(segment) <= 255:
                        backtrack(endi + 1, remainingDots - 1, curstr + segment + ".")
        
        backtrack(0, 4, "")
        return res

