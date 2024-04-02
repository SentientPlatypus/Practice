class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        i = 0
        for s in operations:
            if s in ["X++", "++X"]:
                i += 1
            else:
                i -= 1
        return i