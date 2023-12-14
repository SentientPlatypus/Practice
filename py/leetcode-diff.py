from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = [[0] * len(grid[0]) for _ in range(len(grid))]  # Use list comprehension
        print(diff)
        print(grid)

        onesRow = [0] * len(grid)
        onesCol = [0] * len(grid[0])
        zerosRow = [0] * len(grid)
        zerosCol = [0] * len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    onesRow[r] += 1
                    onesCol[c] += 1
                if grid[r][c] == 0:
                    zerosRow[r] += 1
                    zerosCol[c] += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                diff[r][c] = onesRow[r] + onesCol[c] - zerosRow[r] - zerosCol[c]

        print("onesrow", onesRow)
        print("onesCol", onesCol)

        return diff
