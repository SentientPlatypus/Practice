class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        print(intervals)
        intervals.sort(key=lambda x: x[1])
        print(intervals)

        count = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals [i - 1][1]:
                count += 1
                intervals.pop(i)
                i -= 1
            i += 1
        return count
