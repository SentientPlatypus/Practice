class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_i = 0 #cursors moving through the strings
        p_i = 0
        n = len(s)

        star_i = -1
        s_mismatch_stored = -1
        while s_i < n:
            char = s[s_i]

            if p_i < len(p) and p[p_i] in [char, "?"]:
                p_i += 1
                s_i += 1
            elif p_i < len(p) and p[p_i] == "*":
                #can match to any character
                star_i = p_i
                s_mismatch_stored = s_i
                p_i += 1
            elif star_i != -1:
                #go back to that star
                p_i = star_i + 1
                s_mismatch_stored += 1
                s_i = s_mismatch_stored
            else:
                return False
        return all(x == '*' for x in p[p_i:])


