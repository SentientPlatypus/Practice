class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        count = 0

        for c in s:
            if c == "(": count +=1
            elif c == ")": count -=1
            else: pass
            m = max(count, m)
        
        return m