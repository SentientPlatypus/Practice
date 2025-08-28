class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        # Im going to touch you YES PLEASE YES PLEASE YES PLEASE YES PLEASE

        largest_diag = 0
        res = 0
        
        
        for i in range(len(dimensions)):
            l = dimensions[i][0]
            w = dimensions[i][1]

            diag_squared = l ** 2 + w ** 2

            if diag_squared == largest_diag:
                res = max(res, l * w)

            elif diag_squared > largest_diag:

                res = l * w
                
                largest_diag = diag_squared



        return res