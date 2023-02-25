from sympy import fourier_series


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        return nums



print(Solution.fourSum(None, [1,2,4,3,5,6,4,6], 10))