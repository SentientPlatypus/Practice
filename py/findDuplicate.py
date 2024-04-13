class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        f = 0

        while 1:
            s1 = nums[s1] #traverse once
            f = nums[nums[f]] #traverse twice

            if s1 == f:
                break
        
        while 1:
            s1 = nums[s1]
            s2 = nums[s2]
            if s1 == s2:
                return s1
        
        return 1
        
        
        

