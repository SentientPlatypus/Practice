class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            if n  in m.keys():
                return n
            else:
                m[n] = 1
        return m[-1]