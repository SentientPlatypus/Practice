class Solution:
    def initialStats(self, grid:list[list[int]]):
        nFresh = 0
        nRotten = 0
        rottenPositions = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    nRotten += 1
                    rottenPositions.add((r, c))
                elif grid[r][c] == 1:
                    nFresh += 1
                
        return nFresh, nRotten, rottenPositions

    def neighbors(self, grid:list[list[int]], r, c):
        potential = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        res = []

        for r, c in potential:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                res.append((r,c))
        return res

    def step(self, grid:list[list[int]], nFresh, nRotten, rottenPositions):
        newRottenPositions = set()
        newFresh = nFresh
        newRotten = nRotten

        while rottenPositions:
            cur = rottenPositions.pop()

            for nr, nc in self.neighbors(grid, cur[0], cur[1]):
                if grid[nr][nc] == 1:
                    newFresh -= 1
                    newRotten += 1
                    grid[nr][nc] = 2
                    newRottenPositions.add((nr, nc))

        return newFresh, newRotten, newRottenPositions
        
    def orangesRotting(self, grid: list[list[int]]) -> int:
        res = 0
        nFresh, nRotten, rottenPositions = self.initialStats(grid)

        if not nFresh:
            return 0

        while 1:
            newFresh, newRotten, newRottenPositions = self.step(grid, nFresh, nRotten, rottenPositions)
            print(newFresh)
            res += 1

            if nFresh == newFresh:
                if nFresh != 0:
                    return -1
                break
            
            nFresh, nRotten, rottenPositions = newFresh, newRotten, newRottenPositions
        
        return res - 1




        



        
