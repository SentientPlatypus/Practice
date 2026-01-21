class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            res.append(self.minBitwiseNum(n))
        return res

    
    #111
    #1100
    #1101

    #111
    #110
    #111

    #1011
    #1001
    #1010
    def minBitwiseNum(self, n:int):
        if n % 2 == 0:
            return -1

        minAns = 999999999
        bs = bin(n)[2:]
        for i in range(len(bs)):
            bit = bs[i]
            if bit == "0":
                continue
            else:
                replaced = bs[:i] + "0" + bs[i+1:]
                possibleAns = int(replaced, 2)

                if possibleAns | (possibleAns + 1) == n:
                    minAns = min(minAns, possibleAns)
        return minAns


        
        