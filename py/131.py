class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        curpath = []
        def backtrack(start_i):
            if start_i == len(s):
                res.append(curpath[:])
                return
            
            for end_i in range(start_i, len(s)):
                if s[start_i:end_i + 1] == s[start_i:end_i + 1][::-1]:
                    curpath.append(s[start_i:end_i + 1])
                    backtrack(end_i + 1)
                    curpath.pop()
        
        backtrack(0)
        return res
