class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        N = len(s)

        for i in range(N):
            oddcheck = self.oddCheck(s, i)
            evencheck = self.evenCheck(s, i)

            res = max(res, oddcheck, evencheck, key=lambda x : len(x))
        return res
    
    def oddCheck(self, s: str, i: int) -> int:
            N = len(s)
            l = i
            r = i
            res = 1

            while l - 1 >= 0 and r + 1 < N and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                res += 2
            
            return s[l:r + 1]

    def evenCheck(self, s: str, i: int) -> int:
        N = len(s)
        l = i
        r = i + 1
        res = 0

        while l >= 0 and r < N and s[l] == s[r]:
            l -= 1
            r += 1
            res += 2

        return s[l + 1:r]







        


