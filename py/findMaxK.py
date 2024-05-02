class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        s = set()
        m = -1

        for i in nums:
            s.add(i)
            if -i in s:
                m = max(abs(i), m)

        return m