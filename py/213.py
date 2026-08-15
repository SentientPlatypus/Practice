class Solution:
    def rob1(self, nums:List[int]) ->int:
        N = len(nums)

        if N <= 1:
            return nums[0]

        b4b4 = nums[0]
        b4 = max(nums[1], nums[0])

        for i in range(2, N):
            cur = max(b4b4 + nums[i], b4)
            b4b4 = b4
            b4 = cur

        return b4

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
