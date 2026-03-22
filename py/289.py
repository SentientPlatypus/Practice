class Solution:
    def islivenow(self, board:List[List[int]], r:int, c:int):
        return board[r][c] % 2 == 1
    
    def kill(self, board:List[List[int]], r:int, c:int):
        board[r][c] = 1
    
    def resurrect(self, board:List[List[int]], r:int, c:int):
        board[r][c] += 2      

    def neighbors(self, board:List[List[int]], r:int, c:int):
        n = len(board)
        m = len(board[0])
        res = []
        for i in range(max(0, r-1), min(n, r + 2)):
            for j in range(max(0, c - 1), min(m, c + 2)):
                if (i,j) == (r,c):
                    continue
                res.append((i,j))
        return res

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])

        for r in range(n):
            for c in range(m):
                neighbors = self.neighbors(board, r,c)

                nlive = sum([self.islivenow(board, i,j) for i,j in neighbors])
                ndead = len(neighbors) - nlive

                if self.islivenow(board, r, c):
                    if nlive < 2:
                        self.kill(board, r, c)
                    elif nlive < 4:
                        self.resurrect(board, r, c)
                    else:
                        self.kill(board, r, c)
                else:
                    if nlive == 3:
                        self.resurrect(board, r, c)

        for r in range(n):
            for c in range(m):
                match board[r][c]:
                    case 0:
                        pass
                    case 1:
                        board[r][c] = 0
                    case 2:
                        board[r][c] = 1
                    case 3:
                        board[r][c] = 1
        







        
