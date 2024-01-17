class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        n = {}

        for i in arr:
            if i not in m.keys():
                m[i] = 1
            else:
                m[i] += 1
        
        for i, k in m.items():
            if k not in n.keys():
                n[k] = 1
            else:
                n[k] += 1
        
        return not any(x != 1 for x in n.values())