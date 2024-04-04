class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def neighbors(row, col)-> list[int]:
            return [(r, c) for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if r >= 0 and r < len(image) and c >= 0 and c < len(image[0])]
        start = image[sr][sc]
        q = []
        visited = []


        q.append((sr, sc))

        while q:
            current_r, current_c = q.pop(0)
            visited.append((current_r, current_c))
            value_before_change = image[current_r][current_c]
            image[current_r][current_c] = color

            for n_r, n_c in neighbors(current_r, current_c):
                if image[n_r][n_c] == value_before_change and (n_r, n_c) not in visited :
                    q.append((n_r, n_c))

        return image
