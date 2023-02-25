class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        my_dict = {
            "": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        results = []

        layers = []
        for char in digits:
            layers.append(my_dict[char])

        if len(layers) <= 1:
            return my_dict[digits]

        for i in range(len(layers)):
            if i == 0:
                for letteri in layers[i]:
                    results.append(letteri)
            else:
                new_res = []
                for comb in results:
                    for letter in layers[i]:
                        new_res.append(comb + letter)
                results = new_res
        
        return results


s = Solution()
print(s.letterCombinations("234"))