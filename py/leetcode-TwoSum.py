class Solution:
    def twoSum(self, nums : list[int], target: int) -> list[int]:    
        dictionary = {} #maps value to index
        for n in range(len(nums)):
            complement = target - nums[n] # complement + the value at position n == target
            if complement in dictionary.keys(): #check if complement is in dictionary
                return [n, dictionary[complement]] #if it is, return n, and the index that complement maps to 
            else:
                dictionary[nums[n]] = n



    def twoSumSQ(self, nums : list[int], target: int) -> list[int]:    
        for n in range(len(nums)): # each loop, n will be 0, 1, 2, 3, ... length of nums - 1
            for i in range(n + 1, len(nums)): # each loop, i will be 0, 1, 2, 3, ... length of nums - 1
                if nums[n] + nums[i] == target:
                    return [n, i]

print(Solution.twoSumSQ(self = None, nums = [1,2,3,4,5,6,7,8], target = 6))
