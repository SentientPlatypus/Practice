class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        decomposed_diagonals = [[] for _ in range(2 * n - 1)]

        curpos = [0, n - 1]

        for diag in range(len(decomposed_diagonals)):
            r, c = curpos

            while 0 <= r < n and 0 <= c < n:
                decomposed_diagonals[diag].append(grid[r][c])
                r += 1
                c += 1

            if curpos[1] > 0:
                curpos[1] -= 1
            else:
                curpos[0] += 1


        for i in range(len(decomposed_diagonals)):
            if (i < n - 1):
                decomposed_diagonals[i] = sorted(decomposed_diagonals[i])
            else:
                decomposed_diagonals[i] = sorted(decomposed_diagonals[i], reverse=True)

        res = [[0] * n for _ in range(n)]

        curpos = [0, n - 1]
        for diag in range(len(decomposed_diagonals)):
            r, c = curpos

            for num in decomposed_diagonals[diag]:
                res[r][c] = num
                r += 1
                c += 1

            if curpos[1] > 0:
                curpos[1] -= 1
            else:
                curpos[0] += 1

        return res
