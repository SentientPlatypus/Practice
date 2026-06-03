class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True


class Solution:
    def neighbors(self, r, c):
        res = []
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < len(self.board) and 0 <= nc < len(self.board[0]):
                res.append((nr, nc))
        return res

    def backtrack(self, r, c, node):
        char = self.board[r][c]
        if node.end:
            return True
        
        if char not in node.children:
            return False
        
        child = node.children[char]
        self.board[r][c] = "#"

        for nr, nc in self.neighbors(r, c):
            if self.backtrack(nr, nc, child):
                return True
        self.board[r][c] = char

        return child.end

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        root = TrieNode()
        
        root.insert(word)
        N = len(board)
        M = len(board[0])

        for r in range(N):
            for c in range(M):
                if self.backtrack(r, c, root):
                    return True
        
        return False



