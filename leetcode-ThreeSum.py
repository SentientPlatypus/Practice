# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
import pprint
class Solution:

    # @staticmethod
    # def threeSum(nums: list[int]) -> list[list[int]]:
    #     output_set = []
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for l in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[l] == 0:
    #                     output_set.append(tuple(sorted([nums[i], nums[j], nums[l]])))
    #     output_set = list(map(lambda x: list(x),list([*set(output_set)])))
    #     return output_set
    # WORKS                    

    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:
        """
        threeSum(nums= [-1,0,1,2,-1,-4])
        >>> [[-1, 0, 1], [-1, -1, 2]]
        """
        results = []
        #Hashmap<Value, index>

        occurrences = {}
        for i in range(len(nums)):
            if nums[i] in occurrences.keys():
                occurrences[nums[i]] += 1
            else:
                occurrences[nums[i]] = 1

        dictionary = {}
        #Iterate through to get x
        for x in range(len(nums)):

            target = 0 - nums[x]

            """
            Essentially do twosum with this new target
            """

            "Used<value, bool>"
            copy_of_occurrences = occurrences.copy()
            copy_of_occurrences[nums[x]] = copy_of_occurrences[nums[x]] - 1
            for n in range(x + 1, len(nums)):

                copy_of_occurrences[nums[n]] = copy_of_occurrences[nums[n]] - 1
                complement = target - nums[n] # complement is our third number

                if complement in dictionary.keys() and copy_of_occurrences[complement] != 0: #check if complement is in dictionary
                    results.append(tuple(sorted([nums[n], nums[dictionary[complement]], nums[x]]))) #if it is, return n, and the index that complement maps to 
                else:
                    dictionary[nums[n]] = n

            break
        results = list(map(lambda x: list(x),list([*set(results)])))
        return results



        

print(Solution.threeSum(nums= [-1,0,1]))
