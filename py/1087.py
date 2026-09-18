class Solution:
    def getOptions(self, s: str):
        
        N = len(s)
        res = []
        i = 0
        inBrace = False
        braceOptions = []
        while i < N:
            if s[i] == ",":
                i += 1
                continue
            if not inBrace:
                if s[i] == "{":
                    inBrace = True
                else:
                    res.append(s[i])
            else:
                if s[i] == "}":
                    inBrace = False
                    res.append(braceOptions)
                    braceOptions = []
                else:
                    braceOptions.append(s[i])
            i += 1
        return res

    def expand(self, s: str) -> list[str]:
        lst = self.getOptions(s)
        print(lst)
        N = len(lst)

        res = []
        def backtrack(i, curComb):
            if i == N:
                res.append(curComb)
                return
            else:
                for option in lst[i]:
                    backtrack(i + 1, curComb + option)
        
        backtrack(0, "")
        return sorted(res)
                




