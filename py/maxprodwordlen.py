class Solution:
    def maxProduct(self, words: List[str]) -> int:
        m = {}

        for i in range(len(words)):
            b = 0
            for c in words[i]:
                b |= 1 << (ord(c) - ord('a'))
            m[words[i]] = b
        print(m)
        maxprod = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if m[words[i]] & m[words[j]] == 0:
                    maxprod = max(maxprod, len(words[i]) * len(words[j]))
        return maxprod

                