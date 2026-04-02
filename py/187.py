class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        l = 0
        for r in range(len(s)):
            if r - l + 1 == 10:
                curseq = s[l: r + 1]
                if curseq in seen:
                    res.add(curseq)
                seen.add(curseq)
                l += 1
        
        return list(res)
