class Solution:
    def shiftTransform(self, points:list[list[int]], location:list[int]):
        lx, ly = location
        return [0,0], [[px - lx, py - ly] for px, py in points]
    
    def pointAngle(self, point:list[int]):
        px, py = point
        radians = atan2(py, px)
        deg = degrees(radians)
        return deg

    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        location, points = self.shiftTransform(points, location)
        sameLoc = sum([1 if p == [0,0] else 0 for p in points])
        points = [p for p in points if p != [0,0]]

        points = sorted(points, key=lambda p : self.pointAngle(p))
        angles = sorted([self.pointAngle(p) for p in points])
        angles += [a + 360 for a in angles]

        N = len(angles)

        res = 0
        l = 0
        curAngleSpan = 0
        for r in range(N):
            curAngleSpan = angles[r] - angles[l]

            while curAngleSpan > angle: #angle is fov
                l += 1
                curAngleSpan = angles[r] - angles[l]
            
            res = max(res, r - l + 1)

        return res + sameLoc




