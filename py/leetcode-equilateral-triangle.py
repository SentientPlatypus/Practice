class Solution:
    def triangle(self, l:list) -> list[str]:
        results = []

        layers = []
        for n in l:
            layers.append(n)

        print(layers)

        for i in range(len(layers)):
            if i == 0:
                for letteri in layers[i]:
                    results.append(letteri)
            else:
                new_res = []
                for n in results:
                    for l in layers[i]:
                        new_res.append(n + l)
                results = new_res
        
        return max(results)


s = Solution()
print(s.triangle(
    l = [
    [4, 5, 2, 6, 5],
    [2, 7, 4, 4],
    [8, 1, 0],
    [3, 8],
    [7],
    ]
))