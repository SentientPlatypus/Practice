class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx, ty = target
        drones = list(enumerate(drones))
        inrange = list(filter(lambda d : abs(tx - d[1][0]) + abs(ty - d[1][1]) <= d[1][2], drones))

        if not inrange:
            return -1

        inrange.sort(key = lambda d: abs(tx - d[1][0]) + abs(ty - d[1][1]))
        
        return inrange[0][0]
