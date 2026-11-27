class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = {} #memo[i] returns number of possible combinations in nums that add up to i

        memo[0] = 1

        def M(target:int):
            if target in memo:
                return memo[target]
            
            if target < 0:
                return 0

            total = 0
            for num in nums:
                res = M(target - num)
                total += res
            
            memo[target] = total
            return memo[target]
        
        return M(target)

