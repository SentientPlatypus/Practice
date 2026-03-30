class Solution:

    def needed_swaps(self, chars, max_freq, l, r, newc):
        chars[newc] = chars.get(newc, 0) + 1
        new_maxfreq = max(max_freq, chars[newc])
        windowSize = r - l + 1
        needed = windowSize - new_maxfreq

        #renew old state
        chars[newc] -= 1

        return needed



    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        l = 0
        r = 0
        res = 0

        chars = {}
        max_freq = 0
        while r < n:
            needed = self.needed_swaps(chars, max_freq, l, r, s[r])
            if needed <= k:
                chars[s[r]] += 1
                max_freq = max(max_freq, chars[s[r]])
                res = max(res, r - l + 1)
                r += 1
            else:
                chars[s[l]] -= 1
                l += 1
        return res
