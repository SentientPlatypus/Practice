class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        seen = set()
        l = 0
        max_sum = 0
        current_sum = 0


        for r in range(len(nums)):
            if nums[r] in seen:
                while nums[l] != nums[r]:
                    seen.remove(nums[l])
                    current_sum -= nums[l]
                    l += 1
                current_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            current_sum += nums[r]
            max_sum = max(max_sum, current_sum)
        return max_sum