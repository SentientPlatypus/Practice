class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEndOfWord = False

def insert(root: TrieNode, word: str):
    cur = root
    for char in word:
        idx = ord(char) - ord('a')
        if not cur.children[idx]:
            cur.children[idx] = TrieNode()
        cur = cur.children[idx]
    cur.isEndOfWord = True

class Solution:
    def neighbors(self, board:List[List[str]], r:int, c:int):
        M = len(board)
        N = len(board[0])
        nbrs = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr and nr < M and 0 <= nc and nc < N:
                nbrs.append((nr, nc))
        return nbrs

    def dfs(self, board: List[List[str]], node:TrieNode, path:str, r:int, c:int, res:set):
        char = board[r][c]
        idx = ord(char) - ord('a')
        child = node.children[idx]

        if not child:
            return
        
        path += char
        if child.isEndOfWord:
            res.add(str(path))
        
        board[r][c] = "_" #visited
        for nr, nc in self.neighbors(board, r, c):
            if board[nr][nc] != "_":
                self.dfs(board, child, path, nr, nc, res)
        board[r][c] = char

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            insert(trie, w)
        M = len(board)
        N = len(board[0])

        res = set()
        for r in range(M):
            for c in range(N):
                self.dfs(board, trie, "", r, c, res)

        return list(res)
