class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                #the left half is sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    # target is in the unsorted right hand side.
                    l = mid + 1

            else:
                #right hand side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    #target is in unsorted left half
                    r = mid - 1
        return -1
