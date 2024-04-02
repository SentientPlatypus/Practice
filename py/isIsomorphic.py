class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ts ={}
        st = {}
        for i in range(len(s)):
            if s[i] not in st.keys():
                st[s[i]] = t[i]

                if t[i] not in ts.keys():
                    ts[t[i]] = s[i]
                else:
                    if ts[t[i]] != s[i]:
                        return False
            else:
                if st[s[i]] != t[i]:
                    return False
        print(st)
        return True