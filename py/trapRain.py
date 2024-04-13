class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total = 0
        lmax = -1
        rmax = -1

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                total += lmax - height[l]
                l += 1
            else:
                total += rmax - height[r]
                r -= 1

        return total
        