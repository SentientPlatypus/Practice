class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        maxi = 0
        smaxi = 1 if nums[0] > nums[1] else 0

        lowi = 0
        slowi = 1 if nums[0] < nums[1] else 0

        for i in range(len(nums)):
            if nums[i] > nums[maxi]:
                smaxi = maxi
                maxi = i
            elif nums[i] > nums[smaxi] and i != maxi:
                smaxi = i
            if nums[i] < nums[lowi]:
                slowi = lowi
                lowi = i
            elif nums[i] < nums[slowi] and i != lowi:
                slowi = i

        print(f"maxi: {maxi} smaxi: {smaxi}")
        print(f"lowi: {lowi} slowi: {slowi}")

        return (nums[maxi] * nums[smaxi]) - (nums[lowi] * nums[slowi])