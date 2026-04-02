class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 999999999999

        l = 0
        winsum = 0

        for r in range(len(nums)):
            winsum += nums[r]

            while winsum >= target:
                winlength = r - l + 1
                res = min(res, winlength)

                winsum -= nums[l]
                l += 1
        
        if res == 999999999999:
            return 0
        return res
