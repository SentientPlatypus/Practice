class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
    
    def insert(self, word:str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def neighbors(self, board:List[List[str]], r:int, c:int):
        res = []
        candidates = [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]
        for rp, cp in candidates:
            if 0 <= rp < len(board) and 0 <= cp < len(board[0]):
                res.append((rp, cp))
        return res

    def dfs(self, board:List[List[str]], r:int, c:int, trie:TrieNode, path:str, res:set):
        char = board[r][c]
        
        child = trie.children.get(char, None)
        if not child:
            return 
        
        path += char
        if child.end:
            res.add(path)
        
        #mark visited
        board[r][c] = None
        for rn, cn in self.neighbors(board, r, c):
            if board[rn][cn]:
                self.dfs(board, rn, cn, child, path, res)
        board[r][c] = char
        

        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.insert(w)

        N = len(board)
        M = len(board[0])

        res = set()

        for r in range(N):
            for c in range(M):
                self.dfs(board, r, c, trie, "", res)
        return list(res)
