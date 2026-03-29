class TimeMap:

    def __init__(self):
        self.d = {} #map from key -> [(timestamp, value)]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        timestamps = self.d[key]
        l = 0
        r = len(timestamps) - 1
        max_sat = -1

        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid][0] > timestamp:
                r = mid - 1
            elif timestamps[mid][0] < timestamp:
                max_sat = max(max_sat, mid)
                l = mid + 1 
            else:
                return timestamps[mid][1]


        if max_sat == -1:
            return ""
        return timestamps[max_sat][1]




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
