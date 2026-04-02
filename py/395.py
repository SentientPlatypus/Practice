class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        l = 0
        counts = Counter(s)

        nxtsplts = []
        badchars = [c for c,v in counts.items() if v < k]

        if not badchars:
            return len(s)

        for c in badchars:
            s = s.replace(c, "_")

        nxtsplts += s.split("_")
        
        return max([self.longestSubstring(nxt, k) for nxt in nxtsplts])



