class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        newarray = []

        for i in range(1, len(nums)):
            newarray.append((nums[i] + nums[i - 1]) % 10)
        
        return self.triangularSum(newarray)
