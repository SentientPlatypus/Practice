class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        res = nums[0]
        curmax = nums[0]
        curmin = nums[0]

        for i in range(1, N):

            toConsider = [nums[i], curmax * nums[i], curmin * nums[i]]

            curmax = max(toConsider)
            curmin = min(toConsider)

            res = max(res, curmax)

        return res
