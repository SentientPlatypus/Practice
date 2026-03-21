class Solution:

    def neighbors(self, isConnected:List[List[int]], cur:int):
        n = len(isConnected)

        neighbrs = []
        for i in range(n):
            if isConnected[cur][i]:
                neighbrs.append(i)
        return neighbrs


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited  = set()

        n = len(isConnected)
        res = 0

        for i in range(n):
            if i in visited:
                continue
            
            #node has not been counted in a province yet

            stk = []
            stk.append(i)
            while stk:
                cur = stk.pop()
                visited.add(cur)

                #find neighbors of cur
                for neighbor in self.neighbors(isConnected, cur):
                    if neighbor not in visited:
                        stk.append(neighbor)

            res += 1
        
        return res




