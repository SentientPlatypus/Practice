class Solution:
    def __init__(self):
        self.row_set = set()
        self.col_set = set()
        self.square_set = set()
        self.empty = []

    def init_sets(self, board):
        if not self.row_set and not self.col_set and not self.square_set:
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        n = int(board[r][c])
                        self.row_set.add((r, n))
                        self.col_set.add((c, n))
                        self.square_set.add((r // 3, c // 3, n))
                    else:
                        self.empty.append((r, c))

    def solveSudoku(self, board):
        self.init_sets(board)
        self.solve(board, 0)

    def solve(self, board, i):

        if i == len(self.empty):
            return True

        r, c = self.empty[i]
        for n in range(1, 10):
            inRow = (r, n) in self.row_set
            inCol = (c, n) in self.col_set
            inSquare = (r // 3, c // 3, n) in self.square_set

            if not (inRow or inCol or inSquare):
                board[r][c] = str(n)
                self.row_set.add((r, n))
                self.col_set.add((c, n))
                self.square_set.add((r // 3, c // 3, n))

                if self.solve(board, i + 1):
                    return True

                board[r][c] = "."
                self.row_set.remove((r, n))
                self.col_set.remove((c, n))
                self.square_set.remove((r // 3, c // 3, n))

        return False
    

def main():
    print("wer out")
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

    sol = Solution()
    sol.solveSudoku(board)
    for row in board:
        print(row)

main()