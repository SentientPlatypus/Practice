class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        l = 0
        chars = set()

        for r in range(len(s)):
            rc = s[r]

            while rc in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(rc)
            res = max(r - l + 1, res)
        return res


