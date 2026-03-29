class Solution:
    def numTrips(self, times:List[int], t:int):
        return sum([t // time for time in times])

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = min(time)
        r = min(time) * totalTrips

        while l <= r:
            mid = (l + r) // 2

            feasibleTrips = self.numTrips(time, mid)

            if feasibleTrips < totalTrips:
                # our mid estimate is too low
                l = mid + 1
            else:
                r = mid - 1
        return l


