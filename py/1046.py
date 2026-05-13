class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-stone for stone in stones]
        heapify(hp)

        while len(hp) > 1:
            x = heappop(hp)
            y = heappop(hp)

            if x == y:
                continue
            else:
                heappush(hp, x - y)

        if hp:
            return abs(hp[0])
        return 0
