class Solution:
    def numSquares(self, n: int) -> int:
        memo = {} #returns least number of perfect squares that sum to i

        squares = []
        for i in range(1, n + 1):
            memo[i * i] = 1
            squares.append(i * i)
            if i * i > n:
                break
    
        def M(target:int):
            if target < 0:
                return -1 #not possible
            
            if target in memo:
                return memo[target]
            
            min_squares = float('inf')
            for square in squares:
                subres = M(target - square)
                if subres != -1:
                    min_squares = min(min_squares, 1 + subres)
            
            memo[target] = min_squares
            return memo[target]
        
        return M(n)
