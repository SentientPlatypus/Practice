class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(nopen, nclosed, curstr):
            if nopen + nclosed == n * 2:
                res.append(curstr)
                return
            
            if nopen < n:
                backtrack(nopen + 1, nclosed, curstr + "(")

            if nclosed < nopen: 
                backtrack(nopen, nclosed + 1, curstr + ")")

        
        backtrack(0, 0, "")
        return res

            
