class Solution:

    def getJump(numRows:int) ->int:
        if numRows == 1:
            return 1
        return (numRows - 1) * 2

    def convert(self, s: str, numRows: int) -> str:
    
        res = ""
        jumpby = Solution.getJump(numRows)
        rowcounter = 0
        while rowcounter < numRows:
            index = rowcounter

            if rowcounter == 0 or rowcounter == numRows - 1:
                while index < len(s):
                    current = s[index]
                    res += current
                    index = index + jumpby
            else:
                backtrack = Solution.getJump(rowcounter + 1)
                evenjump = jumpby - backtrack
                oddjump = jumpby - evenjump
                isEven = True
                while index < len(s):
                    current = s[index]
                    res += current
                    if isEven:
                        index += evenjump
                    else:
                        index += oddjump

                    isEven = isEven == False
            rowcounter += 1
        return res
    
if __name__ == "__main__":
    inputs = input()
    inumrows:int = int(input())
    print(Solution().convert(inputs, inumrows))

