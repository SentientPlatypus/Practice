class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        c = 0
        finalC = c
        i = 0
        print(len(s))
        while i < len(s):
            current = s[i]
            try:
                i = d[current] + 1
                finalC = max(c, finalC)
                d = {}
                c = 0
            except:
                d[current] = i
                c += 1
                i += 1
        finalC = max(c, finalC)
        
        return finalC
