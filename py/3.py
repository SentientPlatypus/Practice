class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)

        l = 0
        r = 0
        chars = set()

        while r < n:
            if s[r] not in chars:
                chars.add(s[r])

                res = max(res, len(chars))
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        return res
