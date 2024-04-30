class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        r = 0
        p = 0
        c = [0] * 1024
        c[0] = 1

        for ch in word:
            p ^= 1 << ord(ch) - ord('a')
            r += c[p]
            r += sum(c[p ^1 << i] for i in range(10))
            c[p] += 1
        return r