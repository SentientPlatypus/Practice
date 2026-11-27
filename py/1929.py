class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        N = len(nums)
        res = [0] * 2 * N

        for i in range(N):
            res[i] = nums[i]
            res[i + N] = nums[i]
        
        return res
