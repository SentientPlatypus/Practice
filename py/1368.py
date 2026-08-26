class Direction():
    RIGHT = 1
    LEFT = 2
    DOWN = 3
    UP = 4

class Solution:

    def _gridneighbors(self, grid:List[List[int]], coord):
        r = coord[0]
        c = coord[1]
        unfiltered_ = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        filtered_neighbors = filter(lambda coords: 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0]), unfiltered_)
        return list(filtered_neighbors)
    
    def _freeCell(self, grid:List[List[int]], coord):
        r = coord[0]
        c = coord[1]

        direction = grid[r][c]
        match direction:
            case Direction.RIGHT:
                return (r, c + 1)
            case Direction.LEFT:
                return (r, c - 1)
            case Direction.DOWN:
                return (r + 1, c)
            case Direction.UP:
                return (r - 1, c)

    def minCost(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        dists = {(r,c) : float("inf") for r in range(N) for c in range(M)}
        dists[(0,0)] = 0
        seen = set()

        dq = deque([(0,0)])
        end = (N - 1, M - 1)

        while dq:
            cur = dq.popleft()
            curdist = dists[cur]

            seen.add(cur)
            freecell = self._freeCell(grid, cur)

            if cur == end:
                return dists[cur]

            for neighbor in self._gridneighbors(grid, cur):
                if neighbor in seen:
                    continue
                
                penalty = 0 if neighbor == freecell else 1
                newDist = dists[cur] + penalty

                if newDist < dists[neighbor]:
                    dists[neighbor] = newDist
                    if penalty:
                        dq.append(neighbor)
                    else:
                        dq.appendleft(neighbor)

        return dists[end]



            



