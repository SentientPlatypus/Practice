class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for i in range(start, n + 1):                
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(1, [])
        return res
        
