class Solution:

    def getMaxSum(self, nums:List[int]):
        res = nums[0]
        maxSoFar = nums[0]
        for i in range(1, len(nums)):
            maxSoFar = max(maxSoFar + nums[i], nums[i])
            res = max(res, maxSoFar)
        return res
    
    def getMinSum(self, nums:List[int]):
        res = nums[0]
        minSoFar = nums[0]
        for i in range(1, len(nums)):
            minSoFar = min(minSoFar + nums[i], nums[i])
            res = min(res, minSoFar)
        
        return res

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        

        kanade_max = self.getMaxSum(nums)

        kanade_min = self.getMinSum(nums)

        total_sum = sum(nums)

        return kanade_max if total_sum == kanade_min else max(kanade_max, total_sum - kanade_min)



        
