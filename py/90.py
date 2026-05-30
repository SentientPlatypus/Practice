class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        cur = []
        def backtrack(i):
            res.append(cur.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                cur.append(nums[j])
                backtrack(j + 1)
                cur.pop()
        
        backtrack(0)
        return res
