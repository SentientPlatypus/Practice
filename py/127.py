class Solution:
    def neighbors(self, word:str, wordSet:set) -> List[str]:
        res = []
        N = len(word)

        for pos in range(N):
            for replacementChar in "abcdefghijklmnopqrstuvwxyz":
                if replacementChar == word[pos]:
                    continue

                newWord = word[:pos] + replacementChar + word[pos + 1:]
                if newWord in wordSet:
                    res.append(newWord)

        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0 
        

        q = deque([(beginWord, 1)])
        seen = set()

        while q:
            curWord, curEditDist = q.popleft()
            seen.add(curWord)

            if curWord == endWord:
                return curEditDist
            
            for neighbor in self.neighbors(curWord, wordSet):
                if neighbor not in seen:
                    q.append((neighbor, curEditDist + 1))
        
        return 0
