class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def neighbors(row, col)-> list[int]:
            return [(r, c, board[r][c]) for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if r >= 0 and r < len(board) and c >= 0 and c < len(board[0])]
        

        def check_neighbors(neighbor_list, targetidx):
            if targetidx == len(word):
                return True
            
            q = [(r, c, val) for (r, c, val) in neighbor_list if val == word[targetidx]]
            for (r, c, _) in q:
                board[r][c] = "#"
                if check_neighbors(neighbors(r, c), targetidx + 1):
                    return True
                board[r][c] = word[targetidx]
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    board[r][c] = "#"
                    if check_neighbors(neighbors(r, c), 1):
                        return True
                    board[r][c] = word[0]
        
        return False

