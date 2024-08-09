class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        rbound = len(grid)
        cbound = len(grid[0])

        print(f"this is a {rbound} x {cbound} grid")
        count = 0

        for row in range(0, rbound - 2):
            for col in range(0, cbound - 2):
                if Solution.isMagicSquare(row, col, grid):
                    count  += 1
        
        return count

    
    def isMagicSquare(r: int, c: int, grid: list[list[int]]) -> bool:
        """Returns true if the 3x3 square starting at (r, c) is a magic square."""
        square = [grid[r+i][c:c+3] for i in range(3)]


        row_sum = sum(square[0])
        if any(sum(row) != row_sum for row in square):
            return False
        

        for col in range(3):
            if sum(square[row][col] for row in range(3)) != row_sum:
                return False


        if (square[0][0] + square[1][1] + square[2][2] != row_sum or
            square[0][2] + square[1][1] + square[2][0] != row_sum):
            return False

        all_values = [square[i][j] for i in range(3) for j in range(3)]
        if sorted(all_values) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        
        return True



        