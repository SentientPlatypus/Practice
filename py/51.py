class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [["."] * n for _ in range(n)]
        
        badC = set()
        badPD = set()
        badND = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return res
            
            for c in range(n):
                PD = r + c
                ND = r - c

                if (c not in badC) and (PD not in badPD) and (ND not in badND):
                    board[r][c] = "Q"
                    badC.add(c)
                    badPD.add(PD)
                    badND.add(ND)

                    backtrack(r + 1)

                    board[r][c] = "."
                    badC.remove(c)
                    badPD.remove(PD)
                    badND.remove(ND)
            return
        backtrack(0)
        return res
            
            
        
