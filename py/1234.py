class Solution:
    def balancedString(self, s: str) -> int:
        freqs = Counter(s)
        target = len(s) // 4
        res = float("inf")

        l = 0
        for r in range(len(s)):
            nxt = s[r]
            freqs[nxt] -= 1

            while l < len(s) and all(v <= target for c, v in freqs.items()):
                res = min(res, r - l + 1)
                freqs[s[l]] += 1
                l += 1
        return res
            

            
            
