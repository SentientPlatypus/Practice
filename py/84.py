class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pse = self._pse(heights)
        nse = self._nse(heights)
        print(pse)
        print(nse)
        
        res = 0
        for i in range(len(pse)):
            pi, c, ni = pse[i], heights[i], nse[i]

            leftbound = pi
            rightbound = ni if ni != -1 else len(pse)

            w = rightbound - leftbound - 1
            res = max(w * c, res)

        return res
    
    def _pse(self, heights: List[int]):
        pse = [-1 for h in heights]
        stk = []
        for i in range(len(heights)):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                pse[i] = stk[-1]
            stk.append(i)
        return pse

    def _nse(self, heights: List[int]):
        nse = [-1 for h in heights]
        stk = []
        for i in range(len(heights) - 1, -1, -1):
            while stk and heights[stk[-1]] >= heights[i]:
                stk.pop()
            if stk:
                nse[i] = stk[-1]
            stk.append(i)
        return nse
