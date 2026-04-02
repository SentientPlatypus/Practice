class Solution:
    def get_xth_smallest(self, negf, x):
        for i in range(50, 0, -1):
            x -= negf[i]
            if x <= 0:
                return -i
        return 0

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        l = 0
        negf = [0 for _ in range(51)]

        for r in range(len(nums)):
            rn = nums[r]
            if rn < 0:
                negf[abs(rn)] += 1

            if r - l + 1 < k:
                continue

            res.append(self.get_xth_smallest(negf, x))
            if nums[l] < 0:
                negf[abs(nums[l])] -= 1
            l += 1
        return res

            


        
