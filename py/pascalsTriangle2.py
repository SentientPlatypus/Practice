class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        previous_row = Solution.getRow(self, rowIndex - 1)
        middlepart = []
        for i in range(1, len(previous_row)):
            middlepart.append(previous_row[i - 1] + previous_row[i])
        
        return [1] + middlepart + [1]


        