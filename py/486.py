class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        P1 = 1
        P2 = 0

        def backtrack(p1score, p2score, curturn, l, r):
            if l > r:
                return p1score >= p2score
            
            if curturn == P1:
                takeL = backtrack(p1score + nums[l], p2score, P2, l + 1, r)
                takeR = backtrack(p1score + nums[r], p2score, P2, l, r - 1)
                return takeL or takeR
            else: #its p2
                takeL = backtrack(p1score, p2score + nums[l], P1, l + 1, r)
                takeR = backtrack(p1score, p2score + nums[r], P1, l, r - 1)
                return takeL and takeR

        
        return backtrack(0, 0, P1, 0, len(nums) - 1)
            

        
