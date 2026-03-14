class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = [] #stores indices
        res = [0 for t in temperatures]
        for i, t in enumerate(temperatures):
            if stk:
                while (stk and t > temperatures[stk[-1]]):
                    res[stk[-1]] = i - stk[-1]
                    stk.pop()
            stk.append(i)

        return res
