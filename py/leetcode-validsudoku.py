class Solution:

    def validSquareGroupings(board):
        """CHECKS FOR DUPLICATES IN SQUARE GROUPINGS"""
        for r in range(0,9,3):
            for c in range(0,9,3):
                nums=[board[r+i][c+j] for i in range(3) for j in range(3)]
                s=''.join(nums).replace('.','')
                if not len(s)==len(set(s)):
                    return False
        return True


    def hasDuplicate(r, c, val, board)-> bool:
        """WILL CHECK IF THERE IS A DUPLICATE IN THE ROW AND COLUMN"""

        for elementindex in range(len(board[r])):
            if elementindex != c and board[r][elementindex] == val:
                return True
        
        for rowindex in range(len(board)):
            if rowindex != r:
                if board[rowindex][c] == val:
                    return True
        
        return False


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if Solution.hasDuplicate(r, c, board[r][c], board):
                        return False
        return Solution.validSquareGroupings(board)



if __name__ == "__main__":
    a = input()
    print(Solution().isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))