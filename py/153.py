class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l = 0
        r = n - 1


        #is rotated at least once.
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            
            m = (l + r) // 2

            if nums[m] > nums[r]:
                #minimum element is to the right
                l = m + 1
            elif nums[m] < nums[r]:
                #minimum element is to the left
                r = m
        return nums[l]

        
