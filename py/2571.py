class Solution:
    def minOperations(self, n: int) -> int:
        res = 0

        while n:
            if n & 1: #last bit is 1
                res += 1
                nextbit = n >> 1
                if nextbit & 1: #if the next bit is 1
                    n += 1 #add and carry
                else:
                    n -= 1 #otherwise subtract it
            else:
                n >>= 1
        
        return res


