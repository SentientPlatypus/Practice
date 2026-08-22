class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def backtrack(string:str):
            if string in memo:
                return memo[string]

            if not string:
                return True

            for word in wordDict:
                if string.startswith(word):
                    works = backtrack(string[len(word):])
                    
                    if works:
                        memo[string] = True
                        return True
            
            memo[string] = False
            return False
        
        return backtrack(s)
