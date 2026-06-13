class Emptybin:
    def __init__(self, i):
        self.i = i

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = Emptybin(0)
        memo = {}
        
        def backtrack(i, cursum, res):
            if i == len(nums):
                if cursum == target:
                    return 1
                return 0
            
            if (i, cursum) in memo:
                return memo[(i, cursum)]
            
            add_ways = backtrack(i + 1, cursum + nums[i], res)
            sub_ways = backtrack(i + 1, cursum - nums[i], res)
            
            memo[(i, cursum)] = add_ways + sub_ways
            return memo[(i, cursum)]

        res.i = backtrack(0, 0, res)
        return res.i
        

            

            
