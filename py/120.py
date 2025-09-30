class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        end_row = len(triangle) - 1
        dp = [[99999] * (k + 1) for k in range(len(triangle))]

        
        q = []
        q.append((0,0))
        dp[0][0] = triangle[0][0]

        while q:
            cur_r, cur_c = q.pop()


            if cur_r != end_row:

                if dp[cur_r][cur_c] + triangle[cur_r + 1][cur_c] < dp[cur_r + 1][cur_c]:
                    q.append((cur_r + 1, cur_c))
                    dp[cur_r + 1][cur_c] = dp[cur_r][cur_c] + triangle[cur_r + 1][cur_c]

                if cur_c < len(triangle[cur_r + 1]):
                    if dp[cur_r][cur_c] + triangle[cur_r + 1][cur_c + 1] < dp[cur_r + 1][cur_c + 1]:
                        q.append((cur_r + 1, cur_c + 1))
                        dp[cur_r + 1][cur_c + 1] = dp[cur_r][cur_c] + triangle[cur_r + 1][cur_c + 1]
        
        return min(dp[-1])
            

