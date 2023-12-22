class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        xs = [c[0] for c in points]

        xs.sort()

        maxgap = -1
        for i in range(len(xs) - 1):
            maxgap = max(xs[i+1]-xs[i], maxgap)
        
        return maxgap