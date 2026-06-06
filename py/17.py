class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mapping = {
            "1": [],
            '2': ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(i, curpath):
            if i == len(digits):
                res.append(curpath)
                return
            
            for c in mapping[digits[i]]:
                backtrack(i + 1, curpath + c)
        
        backtrack(0, "")
        return res
