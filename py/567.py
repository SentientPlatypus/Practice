class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = Counter(s1)
        winlen = len(s1)
        l = 0
        r = l + winlen - 1

        chars = Counter(s2[:winlen])

        while r < len(s2):
            if chars == s1f:
                return True
            
            #otherwise we gotta shift the window right.

            chars[s2[l]] -= 1
            if chars[s2[l]] == 0:
                    del chars[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                chars[s2[r]] += 1
        
        return False




            



