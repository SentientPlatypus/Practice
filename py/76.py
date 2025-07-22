from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_set = set(t)
        t_indices = []
        for i, char in enumerate(s):
            if char in t_set:
                t_indices.append(i)


        needed = Counter(t)



        res = 0
        l = 0

        while l <= len(t_indices) - len(t):
            current_count = {c: 0 for c in t_set}
            r = l
            while r < len(t_indices) and current_count[s[t_indices[r]]] < needed[s[t_indices[r]]]:
                current_count[s[t_indices[r]]] += 1
                r += 1
            res = max(res, r - l)
            l += 1
        return res






