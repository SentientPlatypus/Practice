class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        BUY_TYPE = 0

        #heaps store tuples (price, amt)
        sellHeap = [] 
        buyHeap = []
        
        #simulate
        for t in range(len(orders)):

            price, amt, orderType = orders[t]

            if orderType == BUY_TYPE:
                while sellHeap and sellHeap[0][0] <= price and amt > 0:
                    if sellHeap[0][1] > amt:
                        sellHeap[0][1] -= amt
                        amt = 0
                    else:
                        amt -= heappop(sellHeap)[1]
                
                if amt:
                    heappush(buyHeap, [-price, amt])

            else:
                while buyHeap and -buyHeap[0][0] >= price and amt > 0:
                    if buyHeap[0][1] > amt:
                        buyHeap[0][1] -= amt
                        amt = 0
                    else:
                        amt -= heappop(buyHeap)[1]
                
                if amt:
                    heappush(sellHeap, [price, amt])
        
        res = sum([amt for price, amt in sellHeap + buyHeap])
        return res % (10**9 + 7)
