class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def searchFromRoot(self, word, root):
        cur = root
        for i in range(len(word)):
            c = word[i]

            if c == ".":
                return any(self.searchFromRoot(word[i + 1:], child) for child in cur.children.values())

            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        return cur.end

    def search(self, word: str) -> bool:
        return self.searchFromRoot(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
