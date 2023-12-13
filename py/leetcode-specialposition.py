class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        ones = []

        rows = {}
        cols = {}

        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if mat[r][c]:
                    if r in rows.keys():
                        rows[r] += 1
                    else:
                        rows [r] = 1

                    if c in cols.keys():
                        cols[c] += 1
                    else:
                        cols[c] = 1    

                    ones.append([r, c])


        for r, c in ones:
            if rows[r] == 1 and cols[c] == 1:
                count += 1

        return count        
        