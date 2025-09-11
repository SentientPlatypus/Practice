import heapq
class Solution:
    def calculatePassRatio(self, heap:List[List[int]]):
        res = 0
        for gain, p, t in heap:
            res += p / t

        return res / len(heap)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        for p, t in classes:
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        for i in range(extraStudents):
            gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            gain = (p + 1) / (t + 1) - p / t
            heapq.heappush(heap, (-gain, p, t))

        return self.calculatePassRatio(heap)