
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        sx, sy = 0, 0
        s = set()
        s.add((0,0))
        
        for c in path:
            if c == 'N':
                sy += 1
            elif c == 'E':
                sx += 1
            elif c == 'S':
                sy -= 1
            elif c == 'W':
                sx -= 1
            
            p = (sx, sy)
            
            if p not in s:
                s.add(p)
            else:
                return True
        
        return False