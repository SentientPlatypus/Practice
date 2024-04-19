class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    Solution.bfs(r, c, grid)
                    count +=1
        return count


    def bfs(i, j, grid):
        grid[i][j] = "0"
        for r, c in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            if r>=0 and r < len(grid) and c>=0 and c<len(grid[0]) and grid[r][c] == "1":
                Solution.bfs(r, c, grid)
