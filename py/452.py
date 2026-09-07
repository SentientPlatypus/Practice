class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])

        N = len(points)
        res = 0
        i = 0
        while i < N:
            res += 1

            t = points[i][1]
            while i < N and points[i][0] <= t <= points[i][1]:
                i += 1
        
        return res
