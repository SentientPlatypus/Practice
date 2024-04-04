class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('Inf')] * n
        prices[src] = 0

        print(prices)


        for i in range(k + 1):
            temp = prices.copy()


            for s, d, w in flights:
                if prices[s] != float('Inf') and prices[s] + w < temp[d]:
                    temp[d] = prices[s] + w
            
            prices = temp
        

        if prices[dst] == float('Inf'):
            return -1
        return prices[dst]
