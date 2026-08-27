class Solution:
    @staticmethod
    def isPossible(nums:List[int], x:int, y:int, candidate:int):
        "given candidate number of operations, returns if it is possible to reduce all to non positive"
        extraSectionsNeeded = [math.ceil(max(0, n - candidate * y)/(x - y)) for n in nums]
        return sum(extraSectionsNeeded) <= candidate        

    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        l = 0
        r = max(nums)
        res = 0.0

        while l < r:
            mid = (l + r) // 2

            if Solution.isPossible(nums, x, y, mid):
                r = mid
            else:
                l = mid + 1
        
        return r
