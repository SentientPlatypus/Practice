class MinStack:

    def __init__(self):
        self.stk = []
        self.minsofar = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        compareto = val if not self.minsofar else self.getMin()
        self.minsofar.append(min(compareto, val))

    def pop(self) -> None:
        self.stk.pop()
        self.minsofar.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minsofar[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
