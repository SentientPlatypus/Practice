class Fancy:

    def __init__(self):
        self.s = []
        self.add_op = 0
        self.mult_op = 1

    def append(self, val: int) -> None:
        self.s.append((val - self.add_op) * pow(self.mult_op, 10**9 + 7 - 2, 10**9 + 7))

    def addAll(self, inc: int) -> None:
        self.add_op += inc
        self.add_op %= (10**9 + 7)

    def multAll(self, m: int) -> None:
        self.mult_op *= m
        self.mult_op %= (10**9 + 7)
        self.add_op *= m
        self.add_op %= (10**9 + 7)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.s):
            return -1
        val = (self.s[idx] * self.mult_op + self.add_op) % (10**9 + 7)
        return val



# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)