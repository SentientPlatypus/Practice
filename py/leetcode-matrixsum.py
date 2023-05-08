class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        left = [0, 0]
        right = [0, len(mat) - 1]
        for i in range(len(mat)):
            sum += mat[left[0]][left[1]]
            if left != right:
                sum += mat[right[0]][right[1]]
            left[0] += 1
            left[1] += 1
            right[0] += 1
            right[1] -= 1
        return sum