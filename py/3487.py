class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxNum = nums[0]
        seen = set()
        for n in nums:
            maxNum = max(maxNum, n)
            if n > 0 and n not in seen:
                seen.add(n)
        seen.add(maxNum)
        
        return sum(seen)
