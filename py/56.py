class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []


        for strt, end in intervals:
            if not merged or merged[-1][1]  < strt:
                merged.append([strt, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
