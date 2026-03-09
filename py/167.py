class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        l = 0
        r = n - 1

        while l < r:
            cursum = numbers[l] + numbers[r]

            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                #equal
                return [l + 1, r + 1]
        return -1
        

        
