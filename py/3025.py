class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]

                if not (x1 <= x2 and y1 >= y2):
                    continue
                

                validPair = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]
                    if (x1 <= x3 <= x2 and y2 <= y3 <= y1):
                        validPair = False
                        break
                if validPair:
                    count += 1

        return count
