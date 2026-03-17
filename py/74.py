class Solution:

    def convert(self, i, m, n):
        row = ceil(i // n)
        col = i % n
        return row, col

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = (m * n) - 1

        while l <= r:
            mid = (l + r) // 2
            r_mid = self.convert(mid, m, n)
            if target < matrix[r_mid[0]][r_mid[1]]:
                r = mid - 1
            elif target > matrix[r_mid[0]][r_mid[1]]:
                l = mid + 1
            else:
                return True
        return False
        
        


        
        
