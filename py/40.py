class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        curComb = []
        def backtrack(startI, curSum):
            if curSum == target:
                res.append(curComb.copy())
                return
            if curSum > target:
                return
            
            for i in range(startI, len(candidates)):
                if i > startI and candidates[i] == candidates[i - 1]:
                    continue
                    
                curComb.append(candidates[i])
                backtrack(i + 1, curSum + candidates[i])
                curComb.pop()
        
        backtrack(0, 0)
        return res

            

            
        
