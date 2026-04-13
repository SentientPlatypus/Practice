class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = 0 
        f = 0

        while nums[f] and nums[nums[f]]:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break


        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        
        return s
