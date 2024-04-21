from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        mp:dict = {}
        for i, j in edges:
            if i not in mp.keys():
                mp[i] = []
            if j not in mp.keys():
                mp[j] = []
            mp[i].append(j)
            mp[j].append(i)
        
        q = deque()
        v = set()
        v.add(source)
        q.append(source)

        while q:
            c = q.popleft()
            if c == destination:
                return True
            
            for k in mp[c]:
                if k not in v:
                    q.append(k)
                    v.add(k)
        return False