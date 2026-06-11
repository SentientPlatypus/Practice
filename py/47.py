class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [0] * len(nums)

        nums.sort()


        def backtrack(curpath):
            if len(curpath) == len(nums):
                res.append(curpath[:])
                return
            
            for j in range(len(nums)):
                if visited[j] or (j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]):
                    continue
                else:
                    visited[j] = 1
                    curpath.append(nums[j])
                    backtrack(curpath)
                    curpath.pop()
                    visited[j] = 0
            
        backtrack([])
        return res
