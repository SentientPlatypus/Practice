class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        m = {}

        for word in words:
            for c in word:
                if c in m.keys():
                    m[c] += 1
                else:
                    m[c] = 1
        

        total = len(words)
        for _, v in m.items():
            if v % total != 0:
                return False
        return True
        