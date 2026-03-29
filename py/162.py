class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            rightside = nums[mid + 1] if mid + 1 < len(nums) else -float('inf')

            if nums[mid] > rightside:
                #descending slope, must be a peak to the left!
                r = mid - 1
            else:
                l = mid + 1
        return l

