class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ideal = Counter(p)
        res = []
        l = 0
        cur = Counter()

        for r in range(len(s)):
            nxt = s[r]
            cur[nxt] = cur.get(nxt, 0) + 1

            if r - l + 1 < len(p):
                continue

            #otherwise equal, and we will keep it equal
            if cur == ideal:
                res.append(l)
            
            #increment l
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
            l += 1
        return res


        
