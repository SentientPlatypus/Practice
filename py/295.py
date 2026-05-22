class MedianFinder:

    def __init__(self):
        self.maxhp = []
        self.minhp = []

    def addNum(self, num: int) -> None:
        if not self.maxhp or num <= self.maxhp[0]:
            heapq.heappush_max(self.maxhp, num)
        else:
            heapq.heappush(self.minhp, num)
            
        if len(self.maxhp) > len(self.minhp) + 1:
            top = heapq.heappop_max(self.maxhp)
            heapq.heappush(self.minhp, top)
        elif len(self.minhp) > len(self.maxhp) + 1:
            top = heapq.heappop(self.minhp)
            heapq.heappush_max(self.maxhp, top)

    def findMedian(self) -> float:
        if len(self.maxhp) > len(self.minhp):
            return float(self.maxhp[0])
        elif len(self.minhp) > len(self.maxhp):
            return float(self.minhp[0])
            
        return (self.minhp[0] + self.maxhp[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
