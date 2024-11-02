class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not grid[r][c]:
                    continue
                m = max(m, Solution.dfs([r, c], grid))
        return m
    
    def neighbors(r, c, grid):
        return [[x,y] for x, y in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]] if 0 <= x < len(grid) and 0 <= y < len(grid[0])]


    def dfs(coord:list[int], grid):
        total = 0
        q = []
        q.append(coord)
        grid[coord[0]][coord[1]] = 0


        while q:
            cx, cy = q.pop()
            total +=1

            for nx, ny in Solution.neighbors(cx, cy, grid):
                if grid[nx][ny] == 1:
                    q.append([nx, ny])
                    grid[nx][ny] = 0
        
        return total



