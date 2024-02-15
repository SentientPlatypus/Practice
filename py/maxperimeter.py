class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        start = 0
        while start < len(nums):
            total_sum = 0
            for i in range(start + 1, len(nums)):
                total_sum += nums[i]
            
            if total_sum <= nums[start]:
                start += 1
                continue
            else:
                return total_sum + nums[start]
        
        return -1